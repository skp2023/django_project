# Generated by Django 4.2.5 on 2023-09-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='receipe_image',
            field=models.ImageField(upload_to='receipe'),
        ),
    ]