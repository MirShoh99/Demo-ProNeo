from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home(request):
    return render(request, "index.html")

def faculty(request):
    faculties = Faculty.objects.all()
    ctx = {
        "faculties": faculties,
    }
    return render(request, "faculty.html", ctx)


def faculty_create(request):
    model = Faculty()
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("faculty_page")
    ctx = {
        "model": model,
        "form": form,
    }
    return render(request, "form.html", ctx)

def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("faculty_page")
    ctx = {
        "model": model,
        "form": form,
    }
    return render(request, "form.html", ctx)

def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect("faculty_page")


def subject(request):
    return render(request, "subject.html")

def teacher(request):
    return render(request, "teacher.html")

def group(request):
    return render(request, "group.html")

def student(request):
    return render(request, "student.html")

