# Generated by Django 3.1.4 on 2021-02-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20210202_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP адрес'),
        ),
    ]
