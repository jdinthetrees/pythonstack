from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors= {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['f_name']) < 2:
            errors['f_name'] = "First name must be at least two characters"
        if len(postData['l_name']) < 2:
            errors['l_name'] = "Last name must be at least two characters "
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email does not match"
        if len(postData['email']) < 6:
            errors['email_length'] = "Email should be at least six characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least six characters"
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords do not match! try again!"
        return errors

    def login_validator(self, postData):
        errors= {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email does not match"
        if len(postData['email']) < 6:
            errors['email_length'] = "Email should be at least six characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least six characters"
        return errors


    def job_validator(self, postData):
        errors= {}
        if len(postData['title']) < 3:
            errors['title'] = "Title should be at least three characters"
        if len(postData['location']) < 3:
            errors['location'] = "Location should be at least three characters"
        if len(postData['description']) < 3:
            errors['description'] = "Description should be at least three characters"
        return errors


class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name="jobs_uploaded", on_delete = models.CASCADE)
    users = models.ManyToManyField(User, related_name="liked_jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()