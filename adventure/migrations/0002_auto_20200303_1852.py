# Generated by Django 2.2.10 on 2020-03-03 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(default='DEFAULT DESCRIPTION', max_length=500),
        ),
    ]