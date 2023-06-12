from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=40)
    subject = models.CharField(max_length=60)
    description = models.CharField(max_length=500)
    extraDetails = models.CharField(max_length = 500)
    submittions = models.DateTimeField()

