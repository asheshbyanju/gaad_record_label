# Generated by Django 3.0.5 on 2020-05-03 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artists',
            new_name='Artist',
        ),
    ]