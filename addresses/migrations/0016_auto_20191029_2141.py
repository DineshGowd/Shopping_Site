# Generated by Django 2.2.6 on 2019-10-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0015_auto_20191026_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('shipping', 'Shipping'), ('billing', 'Billing')], max_length=120),
        ),
    ]
