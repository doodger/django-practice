# Generated by Django 3.1.1 on 2020-09-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200908_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(null=True, path='None'),
        ),
    ]
