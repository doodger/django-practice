# Generated by Django 3.0.8 on 2020-09-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_linktoproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(),
        ),
    ]