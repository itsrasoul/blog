# Generated by Django 4.1.7 on 2024-02-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0004_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(default=1, upload_to='media/blog_images'),
            preserve_default=False,
        ),
    ]