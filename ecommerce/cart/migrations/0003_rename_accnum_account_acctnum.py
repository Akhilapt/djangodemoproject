# Generated by Django 5.0.1 on 2024-02-02 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_account_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='accnum',
            new_name='acctnum',
        ),
    ]
