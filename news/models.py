from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 500)
    post = models.TextField()
    date = models.DateTimeField()
    image=models.ImageField("Изображение", upload_to="media/")


    def __str__(self):
        return self.title
