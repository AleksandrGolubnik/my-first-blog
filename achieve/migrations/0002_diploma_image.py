# Generated by Django 2.2.2 on 2019-06-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achieve', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diploma',
            name='image',
            field=models.ImageField(default=True, upload_to='media/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
