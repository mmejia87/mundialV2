# Generated by Django 4.1 on 2022-09-03 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='selecciones'),
        ),
    ]
