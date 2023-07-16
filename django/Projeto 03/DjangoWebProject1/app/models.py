"""
Definition of models.
"""

from django.db import models


class Usuario(models.Model):
    login = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return self.login