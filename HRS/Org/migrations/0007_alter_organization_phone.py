# Generated by Django 4.2.10 on 2024-02-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Org', '0006_alter_organization_org_id_alter_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
