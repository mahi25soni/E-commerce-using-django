# Generated by Django 4.0.4 on 2022-12-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_cart_no_of_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='no_of_items',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
