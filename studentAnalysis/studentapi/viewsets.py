from rest_framework import viewsets
from .import models
from .import serializers

class StudentViewset(viewsets.ModelViewSet):
    queryset = models.student_list_table.objects.all()
    serializer_class = serializers.Studentserializer