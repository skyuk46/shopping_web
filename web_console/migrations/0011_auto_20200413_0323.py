# Generated by Django 3.1.dev20200307214613 on 2020-04-12 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0010_products_abc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='abc',
            new_name='images',
        ),
    ]
