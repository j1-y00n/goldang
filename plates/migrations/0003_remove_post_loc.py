# Generated by Django 3.2.18 on 2023-05-04 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plates', '0002_post_visited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='loc',
        ),
    ]
