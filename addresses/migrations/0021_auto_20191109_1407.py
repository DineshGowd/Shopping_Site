# Generated by Django 2.2.6 on 2019-11-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0020_auto_20191109_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
    ]
