from django.db import models

class ActiveSessionUser(models.Model):
    name = models.CharField(max_length=100)
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
