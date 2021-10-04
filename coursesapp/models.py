from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Category(models.Model):
	name = models.CharField(max_length=50, blank=True, default='')
	imgpath = models.TextField()

class Branch(models.Model):
	latitude = models.CharField(max_length=100, blank=True, default='')
	longitude = models.CharField(max_length=100, blank=True, default='')
	address = models.TextField()

class Contact(models.Model):
	type = models.SmallIntegerField()
	value = models.TextField()

class Course(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    logo = models.TextField()
    contacts = models.ForeignKey(Contact, on_delete = models.CASCADE)
    branches = models.ForeignKey(Branch, on_delete = models.CASCADE)

    class Meta:
        ordering = ['name']



