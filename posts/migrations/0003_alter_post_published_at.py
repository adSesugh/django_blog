# Generated by Django 4.2.2 on 2023-06-23 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_published_post_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
