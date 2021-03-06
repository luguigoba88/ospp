# Generated by Django 3.2.7 on 2021-09-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('CustomerId', models.AutoField(primary_key=True, serialize=False)),
                ('CustomerName', models.CharField(max_length=100)),
                ('CustomerName2', models.CharField(max_length=100)),
                ('CustomerName3', models.CharField(max_length=100)),
                ('Surname', models.CharField(max_length=100)),
                ('DateOfJoining', models.DateField()),
                ('Street', models.CharField(max_length=100)),
                ('Number', models.CharField(max_length=100)),
                ('Suburb', models.CharField(max_length=100)),
                ('ZipCode', models.CharField(max_length=100)),
                ('PhotoFileName', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StatusCatalogs',
            fields=[
                ('CatalogId', models.AutoField(primary_key=True, serialize=False)),
                ('DescriptionName', models.CharField(max_length=100)),
            ],
        ),
    ]
