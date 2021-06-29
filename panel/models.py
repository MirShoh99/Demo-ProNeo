from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name

class Cafedra(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    subject = models.ForeignKey(Subject, blank=False, null=True, on_delete=models.SET_NULL)
    cafedra = models.ForeignKey(Cafedra, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Group(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    faculty = models.ForeignKey(Faculty, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    group = models.ForeignKey(Group, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
