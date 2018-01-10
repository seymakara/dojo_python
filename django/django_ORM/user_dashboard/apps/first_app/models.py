from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r"^[a-zA-Z\s]+$")

class UserManager(models.Manager):
    def regvalidator(self, postData):
        errors = {}
        if len(postData["first_name"]) < 1:
            errors["first_name"] = "First name is required."
        elif len(postData["first_name"]) < 2:
            errors["first_name"] = "First name must contain at least two characters."
        elif not NAME_REGEX.match(postData["first_name"]):
            errors["first_name"] = "First name contains invalid characters."

        if len(postData["last_name"]) < 1:
            errors["last_name"] = "Last name is required."
        elif len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name must contain at least two characters."
        elif not NAME_REGEX.match(postData["last_name"]):
            errors["last_name"] = "Last name contains invalid characters."

        if len(postData["email"]) < 1:
            errors["email"] = "Email is required."
        elif not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Invalid email address."

        if len(postData["pw"]) < 8:
            errors["pw"] = "Password must contain at least 8 characters."
        elif not postData["pw"] == postData["pw_confirm"]:
            errors["pw"] = "Password and confirmation do not match."

        if not errors and User.objects.filter(email=postData["email"]):
            errors["email"] = "Email address is already in use."

        return errors

    def logvalidator(self, postData):
        try:
            user_to_login = User.objects.get(email = postData["email"])
            if bcrypt.checkpw(postData['pw'].encode(), user_to_login.password.encode()):
                return user_to_login
        except:
            pass
        return "Invalid email or password."
    
    def pw_changevalidator(self, postData):
        errors = {}
        if len(postData["pw"]) < 8:
            errors["pw"] = "Password must contain at least 8 characters."
        elif not postData["pw"] == postData["pw_confirm"]:
            errors["pw"] = "Password and confirmation do not match."
        return errors



class User(models.Model):
    user_level = models.IntegerField(default=1)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    message = models.TextField(max_length=255)
    sender = models.ForeignKey(User, related_name="sent_messages")
    receiver = models.ForeignKey(User, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

class Comment(models.Model):
    comment = models.TextField(max_length=255)
    sender = models.ForeignKey(User, related_name="sent_comments")
    message = models.ForeignKey(Message, related_name="message_comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

