# Generated by Django 3.0.3 on 2020-05-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0024_userdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='number',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]