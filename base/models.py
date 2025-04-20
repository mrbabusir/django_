from django.db import models

# Create your models here.
class Todolist(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    def __str__ (self):
        return (f"{self.title},{self.is_completed}")