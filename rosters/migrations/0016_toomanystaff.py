# Generated by Django 2.2.3 on 2019-07-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rosters', '0015_toomanystaff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslot',
            name='max_staff',
        ),
        migrations.AddField(
            model_name='shift',
            name='max_staff',
            field=models.IntegerField(default=5),
        ),
    ]