from django.db import models

class Diploma(models.Model):
    title=models.CharField(max_length=1500)
    date=models.DateTimeField()
    image=models.ImageField("Изображение", upload_to="media/")


    def __str__(self):
        return self.title
