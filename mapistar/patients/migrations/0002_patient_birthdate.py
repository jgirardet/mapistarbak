# Generated by Django 2.0.2 on 2018-02-08 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2018, 2, 8, 11, 40, 41, 497145)),
            preserve_default=False,
        ),
    ]
