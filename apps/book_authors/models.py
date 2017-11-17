from __future__ import unicode_literals

from django.db import models

  # Create your models here.

class books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    book = models.ManyToManyField(books, related_name="publishers")

    
#ninja3= ninjas.objects.create(first_name="shell",last_name="cruise",dojo=dojos.objects.get(id=3))

   

