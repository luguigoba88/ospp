# Generated by Django 3.2.7 on 2021-09-28 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0009_alter_customers_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='Group',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
