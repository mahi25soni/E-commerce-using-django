# Generated by Django 4.0.4 on 2022-12-13 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_buyerhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerhistory',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 12, 13, 23, 14, 16, 624964)),
        ),
    ]
