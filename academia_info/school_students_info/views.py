from django.http import HttpResponse
from django.core import serializers
from rest_framework.viewsets import ModelViewSet

from .models import School, Student, StudentDetail
from .serializers import SchoolSerializer, StudentSerializer, StudentDetailSerializer

import logging

logger = logging.getLogger(__name__)


class StudentViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SchoolViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class FilteredStudentViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs["schools_pk"])


class StudentDetailViewSet(ModelViewSet):
    serializer_class = StudentDetailSerializer

    def get_queryset(self):
        student_details = StudentDetail.objects.filter(
            student=self.kwargs["students_pk"]
        )
        return student_details
