# Generated by Django 3.1.dev20200307214613 on 2020-04-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0014_auto_20200414_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(default=None, height_field=600, upload_to='pictures/', width_field=600),
        ),
    ]
