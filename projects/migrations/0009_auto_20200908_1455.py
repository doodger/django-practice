# Generated by Django 3.1.1 on 2020-09-08 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200908_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.TextField(),
        ),
    ]
