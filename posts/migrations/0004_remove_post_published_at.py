# Generated by Django 4.2.2 on 2023-06-26 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_published_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_at',
        ),
    ]
