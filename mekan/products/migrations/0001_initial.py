# Generated by Django 3.1 on 2020-08-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('picture', models.ImageField(blank=True, upload_to='')),
                ('description', models.TextField(max_length=72)),
                ('price', models.FloatField()),
                ('ingredients', models.ManyToManyField(to='products.Ingredient')),
            ],
        ),
    ]