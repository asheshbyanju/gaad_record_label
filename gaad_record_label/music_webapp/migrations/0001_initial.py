# Generated by Django 3.0.5 on 2020-05-02 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('nationality', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]