# Generated by Django 3.1.dev20200307214613 on 2020-04-25 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_console', '0022_auto_20200425_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_cart',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='productCart', to='web_console.Products'),
        ),
    ]