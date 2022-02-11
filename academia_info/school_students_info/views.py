from datetime import date, datetime
import logging

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer

logger = logging.getLogger(__name__)


class StudentViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = StudentSerializer(queryset, many=True)
        today = date.today()
        for data in serializer.data:
            if data.get("birthdate"):
                born = datetime.strptime(data["birthdate"], "%Y-%m-%d")
                data["age"] = (
                    today.year
                    - born.year
                    - ((today.month, today.day) < (born.month, born.day))
                )
                data.move_to_end("school")
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StudentSerializer(instance=instance)
        data = serializer.data
        if data.get("birthdate"):
            today = date.today()
            born = datetime.strptime(data["birthdate"], "%Y-%m-%d")
            data["age"] = (
                today.year
                - born.year
                - ((today.month, today.day) < (born.month, born.day))
            )
        return Response(data)


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

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = StudentSerializer(queryset, many=True)
        today = date.today()
        for data in serializer.data:
            if data.get("birthdate"):
                born = datetime.strptime(data["birthdate"], "%Y-%m-%d")
                data["age"] = (
                    today.year
                    - born.year
                    - ((today.month, today.day) < (born.month, born.day))
                )
                data.move_to_end("school")
        return Response(serializer.data)
