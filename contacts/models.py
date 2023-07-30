from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)