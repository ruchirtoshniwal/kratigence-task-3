# Generated by Django 3.1.2 on 2020-12-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='resume',
            field=models.FileField(upload_to='documents/'),
        ),
    ]
