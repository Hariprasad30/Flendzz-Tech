from rest_framework import serializers
from .models import student_list_table

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student_list_table
        fields = '__all__'