from django.db import models
import re

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

    def book_validator(self, postData):
        errors= {}
        if len(postData['title']) < 6:
            errors['title'] = "Email should be at least five characters"
        if len(postData['description']) < 6:
            errors['description'] = "Password should be at least five characters"
        return errors

    



class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


# Create your models here.
