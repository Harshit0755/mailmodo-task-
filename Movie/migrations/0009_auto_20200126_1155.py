# Generated by Django 3.0.1 on 2020-01-26 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0008_auto_20200126_1151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='showtime',
            name='time1',
        ),
        migrations.RemoveField(
            model_name='showtime',
            name='time2',
        ),
        migrations.RemoveField(
            model_name='showtime',
            name='time3',
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(blank=True, null=True)),
                ('show', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Movie.ShowTime')),
            ],
        ),
    ]
