from __future__ import unicode_literals

from django.db import models


class CourseManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['name']) < 5:
            errors.append("Name field must be 5 characters or more!")
        if len(post_data['description']) < 15:
            errors.append("Description field must be 15 characters or more")
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Description(models.Model):
    text = models.TextField()
    belongsto = models.OneToOneField(Course)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Comment(models.Model):
    text = models.TextField()
    belongsto = models.ForeignKey(Course, related_name = "comments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)