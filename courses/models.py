from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    semester = models.IntegerField()
    year = models.IntegerField()
    seats_available = models.IntegerField()
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.code} ({self.name})'

class QuotaRequest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quota_request')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.course}'