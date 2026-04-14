from django.db import models
from django.contrib.auth.hashers import make_password, check_password as _check

class CUser(models.Model):
    username       = models.CharField(max_length=100, unique=True)
    email          = models.EmailField(unique=True)
    password_hash  = models.CharField(max_length=255)  # stores the hashed value
    created_at     = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        """Hash and store the password."""
        self.password_hash = make_password(raw_password)

    def check_password(self, raw_password):
        """Verify a raw password against the stored hash."""
        return _check(raw_password, self.password_hash)

    def __str__(self):
        return self.username
