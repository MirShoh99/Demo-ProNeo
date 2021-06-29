from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home_page"),
    path("faculty/", faculty, name="faculty_page"),
    path("faculty/create/", faculty_create, name="faculty_create"),
    path("faculty/<int:pk>/edit/", faculty_edit, name="faculty_edit"),
    path("subject/", subject, name="subject_page"),
    path("teacher/", teacher, name="teacher_page"),
    path("group/", group, name="group_page"),
    path("student/", student, name="student_page"),
]