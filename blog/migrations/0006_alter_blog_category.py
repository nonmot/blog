# Generated by Django 3.2 on 2021-05-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210509_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(blank=True, to='blog.Category', verbose_name='カテゴリー'),
        ),
    ]
