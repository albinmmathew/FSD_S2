from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.full_name
