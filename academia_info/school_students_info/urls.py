from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import (
    StudentViewSet,
    SchoolViewSet,
    FilteredStudentViewSet,
    StudentDetailViewSet,
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"schools", SchoolViewSet)

schools_router = routers.NestedSimpleRouter(router, r"schools", lookup="schools")
schools_router.register(r"students", FilteredStudentViewSet, basename="school-students")

students_router = routers.NestedSimpleRouter(
    schools_router, r"students", lookup="students"
)
students_router.register(r"details", StudentDetailViewSet, basename="student-details")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(schools_router.urls)),
    path("", include(students_router.urls)),
]
