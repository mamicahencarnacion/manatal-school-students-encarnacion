from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import FilteredStudentViewSet, SchoolViewSet, StudentViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"schools", SchoolViewSet)

schools_router = routers.NestedSimpleRouter(router, r"schools", lookup="schools")
schools_router.register(r"students", FilteredStudentViewSet, basename="school-students")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(schools_router.urls)),
]
