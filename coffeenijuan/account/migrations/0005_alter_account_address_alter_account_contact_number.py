# Generated by Django 4.0.2 on 2022-03-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_account_is_verified_alter_account_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AlterField(
            model_name='account',
            name='contact_number',
            field=models.CharField(default='None', max_length=30),
        ),
    ]
