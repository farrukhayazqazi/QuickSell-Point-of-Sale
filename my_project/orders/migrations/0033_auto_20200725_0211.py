# Generated by Django 3.0.3 on 2020-07-25 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_auto_20200725_0209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='product',
            new_name='productID',
        ),
    ]