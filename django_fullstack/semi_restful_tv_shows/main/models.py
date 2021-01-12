from django.db import models
import re

class UserManager(models.Manager):
    def show_validator(self, postData):
        errors= {}
        if len(postData['title']) < 3:
            errors['title'] = "Title must be at least three characters"
        if len(postData['network']) < 2:
            errors['network'] = "Network must be at least two characters "
        if len(postData['description']) < 10:
            errors['description'] = "Description should be at least ten characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    


# Create your models here.
