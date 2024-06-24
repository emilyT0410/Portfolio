from django.db import models


# Create your models here.
class User(models.Model):
    """Class for the user. Each user has username, password and email address"""

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.username


class StickyNote(models.Model):
    """Class for sticky note. Each note has a title,
    description and when it was created"""

    title = models.CharField(max_length=30, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
