from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User
from django.contrib import messages

# Create your models here.
class QuoteManager(models.Manager):
    def create_quote(self, data):
        errors=[]
        if len(data['quoted_by']) < 3 or len(data['message']) < 10:
            errors.append("No empty entries!")
        if not errors:
            return(True, data)
        return(False, errors)

class Quote(models.Model):
    quoted_by = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    quote_creator_id = models.ForeignKey("loginreg.User", related_name="quote_creator")
    quote_joiner_id = models.ManyToManyField("loginreg.User", related_name="quote_joiner")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quoteManager = QuoteManager()
    objects = models.Manager()
