from django.db import models
from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone 

class Tag(models.Model):
    tag = models.CharField(max_length=128)

    class Meta:
        ordering = ['tag']

    def __str__(self):
        return f"{self.tag}"


class Post(models.Model):
    title = models.CharField(max_length=128)
    description = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"Id:{self.pk} | {self.title} | {self.created_at} | {self.updated_at}"

