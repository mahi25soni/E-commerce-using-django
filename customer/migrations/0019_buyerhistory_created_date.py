# Generated by Django 4.0.4 on 2022-12-13 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_remove_buyerhistory_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyerhistory',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
