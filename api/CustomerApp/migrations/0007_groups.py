# Generated by Django 3.2.7 on 2021-09-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0006_auto_20210928_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('GroupsId', models.AutoField(primary_key=True, serialize=False)),
                ('GroupName', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
