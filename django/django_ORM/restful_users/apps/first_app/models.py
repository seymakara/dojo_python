from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validate(self, post_data):
        errors = {}
        for field, value in post_data.iteritems():

            # check all fields for emptyness
            if len(value) < 1:
                errors[field] = "{} field is required".format(field)

            # check name fields for min length
            if field == "firstname" or field == "lastname":
                if not field in errors and len(value) < 3:
                    errors[field] = "{} field must bet at least 3 characters".format(field)

        # check email field for valid email
        if not "email" in errors and not re.match(EMAIL_REGEX, post_data['email']):
            errors['email'] = "invalid email"
        
        # if email is valid check db for existing email
        else:
            if len(self.filter(email=post_data['email'])) > 0:
                errors['email'] = "email already in use"

        return errors
    
    def update_validate(self, post_data):
        errors = {}
        for field, value in post_data.iteritems():

            # check all fields for emptyness
            if len(value) < 1:
                errors[field] = "{} field is required".format(field)

            # check name fields for min length
            if field == "firstname" or field == "lastname":
                if not field in errors and len(value) < 3:
                    errors[field] = "{} field must bet at least 3 characters".format(field)

        # check email field for valid email
        if not "email" in errors and not re.match(EMAIL_REGEX, post_data['email']):
            errors['email'] = "invalid email"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    #you declare what to print from an object
    def __str__(self):
        return self.first_name
