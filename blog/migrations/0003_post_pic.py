# Generated by Django 3.1.2 on 2020-10-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201026_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.ImageField(default='default.jpeg', upload_to='post_pics'),
        ),
    ]