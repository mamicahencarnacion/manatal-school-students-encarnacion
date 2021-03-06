from datetime import date

from django.db import models
from django_countries.fields import CountryField

from .validators import validate_greater_than_zero


class School(models.Model):
    name = models.CharField(max_length=20)
    max_students = models.PositiveBigIntegerField(
        validators=[validate_greater_than_zero]
    )
    students_counter = models.PositiveBigIntegerField(editable=False, default=0)

    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.CharField(max_length=20, editable=False, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    nationality = CountryField(default="PH")
    birthdate = models.DateField(null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
