# Generated by Django 3.2.7 on 2021-09-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0002_customers_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='PhotoFileName',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
