# Generated by Django 3.1.3 on 2024-07-14 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='contnet',
            new_name='content',
        ),
    ]
