# Generated by Django 4.2.10 on 2024-02-08 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Org', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='valid_until',
            field=models.DateField(),
        ),
    ]