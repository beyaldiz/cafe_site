# Generated by Django 3.1 on 2020-08-24 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200824_1111'),
        ('order', '0002_auto_20200824_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
    ]
