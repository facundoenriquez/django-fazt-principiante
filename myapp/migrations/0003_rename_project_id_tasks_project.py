# Generated by Django 5.0.4 on 2024-04-21 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_tasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='project_id',
            new_name='project',
        ),
    ]
