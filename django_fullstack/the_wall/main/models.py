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
        

class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
