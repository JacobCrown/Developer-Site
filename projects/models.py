from tkinter import CASCADE
from django.db import models
import uuid

class Project(models.Model):
    title = models.CharField(max_length=200)
    # null - can be empty in database, blank - form field can be empty
    description = models.TextField(null=True, blank=True) 
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, # encoding type
        unique=True,
        primary_key=True, # use this field as primary key
        editable=False, # cannot modify this in forms
        )

    def __str__(self):
        return self.title


class Reviev(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote'),
    )
    # owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True) 
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    id = models.UUIDField(
        default=uuid.uuid4, # encoding type
        unique=True,
        primary_key=True, # use this field as primary key
        editable=False, # cannot modify this in forms
        )

    def __str__(self):
        return self.value