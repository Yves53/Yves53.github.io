from __future__ import unicode_literals
import re
import bcrypt
from django.db import models
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        if len(self.filter(email=post_data['email'])) > 0:
            # check this user's password
            user = self.filter(email=post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('email/password incorrect')
        else:
            errors.append('email/password incorrect')

        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = []
        if len(post_data['name']) < 2:
            errors.append("name fields must be at least 3 characters")
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("invalid email!")
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("email already in use")
        if post_data['password'] != post_data['password_confirm']:
            errors.append("passwords do not match")
        if not post_data['dob'] or not datetime.strptime(post_data['dob'], "%Y-%m-%d") > datetime.today():
            errors.append('Your date or birth cannot be empty or before today')
        if not errors:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                name=post_data['name'],
                email=post_data['email'],
                alias=post_data['alias'],
                password=hashed,
                dob=post_data['dob']
            )
            return new_user
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, default=None)
    password = models.CharField(max_length=255)
    dob = models.DateField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.email


class Quotes(models.Model):
    quoted_by = models.CharField(max_length=255)
    quote = models.TextField()
    usr = models.ForeignKey(User)
    favorites = models.ManyToManyField(User, related_name='user_favorites')
