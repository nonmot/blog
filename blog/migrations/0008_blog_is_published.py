# Generated by Django 3.2 on 2021-08-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blog_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='公開フラグ'),
        ),
    ]
