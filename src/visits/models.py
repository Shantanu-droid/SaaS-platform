from django.db import models

# Create your models here.

class PageVisit(models.Model):
    '''track user visits per page'''
    page = models.TextField(null=True, blank=True)
    timstamp = models.DateTimeField(auto_now=True)
