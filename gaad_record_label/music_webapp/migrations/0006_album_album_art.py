# Generated by Django 3.0.5 on 2020-05-03 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_webapp', '0005_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_art',
            field=models.ImageField(blank=True, upload_to='album'),
        ),
    ]