# Generated by Django 2.2.6 on 2019-10-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0016_auto_20191029_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120),
        ),
    ]