from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"
