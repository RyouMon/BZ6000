from django.db import models
from tinymce.models import HTMLField
# Put tinymce in media/js.
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = HTMLField()
