# Generated by Django 3.2.7 on 2021-09-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomerApp', '0005_auto_20210928_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='StatusBC',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='StatusPLD',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='StatusWL',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
