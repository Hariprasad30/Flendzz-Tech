from django.db import models

# Create your models here.
class student_list_table(models.Model):
    student = models.CharField(max_length=200,unique=True, null=True, blank=True)
    name = models.CharField(max_length=200, unique=True, null=True, blank=True)
    rollNumber = models.CharField(max_length=8)
    marks = models.CharField(max_length=100)
