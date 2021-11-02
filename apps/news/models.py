from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.related import ForeignKey

class News(models.Model):
    title = models.CharField(max_length = 255)
    short_description = models.TextField(blank = True)
    full_description = models.TextField(blank = True)
    type = ForeignKey('Types', on_delete = DO_NOTHING)

    def __str__(self):
        return self.title

class Types(models.Model):
    name = models.CharField(max_length = 255, primary_key = True)
    color = models.CharField(max_length = 50)

    def __str__(self):
        return self.name