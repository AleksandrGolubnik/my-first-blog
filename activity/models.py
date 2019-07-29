from django.db import models
from django.forms import ModelForm


class Upload(models.Model):
    title = models.CharField(max_length = 500, default='')
    discription = models.TextField(default='')
    pic = models.FileField(upload_to='files/',default=' ')

    def save(self, *args, **kwargs):
        super(Upload, self).save(*args, **kwargs)
        filename = self.pic.url
    def __str__(self):
        return self.title
