import logging
from datetime import date, datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import School, Student

logger = logging.getLogger(__name__)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def create(self, validated_data):
        # Get the school ID from the request body
        school = validated_data["school"]
        school_id = school.id
        # Get the school ID from the URL
        request_kwargs = self.context.get("request").parser_context.get("kwargs")
        request_school_pk = request_kwargs.get("schools_pk") or None
        if request_school_pk and int(request_school_pk) != school_id:
            logger.exception(
                "School ID in the URL does not match the school ID from the request body.",
                extra={
                    "request_body_school_id": request_school_pk,
                    "url_school_id": school_id,
                },
            )
            raise ValidationError("Cannot create student.")

        # Filter and count students from the school
        current_students = Student.objects.filter(school=school).count()
        if current_students >= school.max_students:
            logger.exception(
                "Maximum number of students in school has been reached.",
                extra={"max_students": school.max_students, "school_id": school_id},
            )
            raise ValidationError("Maximum number of students reached.")
        counter = school.students_counter + 1

        if not counter:
            raise ValidationError("Counter not found")

        # Create student ID and student instance
        validated_data["student_id"] = f"{date.today().year}{school_id:06}{counter:010}"
        student = Student.objects.create(**validated_data)

        # Update counter of students in School instance
        school.students_counter = counter
        school.save(update_fields=["students_counter"])

        return student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
