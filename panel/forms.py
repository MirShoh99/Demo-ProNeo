from django import forms
from .models import *

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"