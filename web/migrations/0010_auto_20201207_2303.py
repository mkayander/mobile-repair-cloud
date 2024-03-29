# Generated by Django 3.1.4 on 2020-12-07 20:03

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20201206_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackrequest',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='feedbackrequest',
            name='message',
            field=models.TextField(null=True, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='feedbackrequest',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Номер телефона'),
        ),
    ]
