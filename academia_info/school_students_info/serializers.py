import logging
from datetime import date

from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotFound

from .models import School, Student, StudentDetail

logger = logging.getLogger(__name__)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        school = validated_data["school"]
        school_id = school.id
        request_kwargs = self.context.get("request").parser_context.get("kwargs")
        request_school_pk = request_kwargs.get("schools_pk") or None
        if request_school_pk and int(request_school_pk) != school_id:
            logger.exception("")
            raise ValidationError("Cannot create student.")

        current_students = Student.objects.filter(school=school).count()
        if current_students >= school.max_students:
            raise ValidationError("Maximum number of students reached.")
        counter = school.students_counter + 1

        if not counter:
            raise ValidationError("Counter not found")

        validated_data["student_id"] = f"{date.today().year}{school_id:06}{counter:010}"
        student = Student.objects.create(**validated_data)
        StudentDetail.objects.create(**{"student": student})

        school.students_counter = counter
        school.save(update_fields=["students_counter"])

        return student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = "__all__"
        depth = 1

    def create(self, validated_data):
        request_kwargs = self.context.get("request").parser_context.get("kwargs")
        student_id = request_kwargs.get("students_pk")
        if not student_id:
            logger.exception("")
            raise NotFound("Student not found!")

        student_detail = StudentDetail.objects.filter(student=student_id).get()
        fields = []

        if validated_data.get("birthdate"):
            today = date.today()
            born = validated_data["birthdate"]
            student_detail.birthdate = born
            student_detail.age = (
                today.year
                - born.year
                - ((today.month, today.day) < (born.month, born.day))
            )
            fields.extend(["birthdate", "age"])
        if validated_data.get("nationality"):
            student_detail.nationality = validated_data.get("nationality")
            fields.append("nationality")

        student_detail.save(update_fields=fields)

        return student_detail
