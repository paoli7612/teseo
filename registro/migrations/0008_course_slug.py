# Generated by Django 3.2.16 on 2022-11-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0007_alter_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(blank=True, max_length=16, unique=True),
        ),
    ]
