# Generated by Django 3.1.2 on 2020-10-26 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Title',
            new_name='title',
        ),
    ]