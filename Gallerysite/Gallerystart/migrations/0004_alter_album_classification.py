# Generated by Django 4.1.3 on 2023-12-08 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallerystart', '0003_alter_album_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='classification',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
