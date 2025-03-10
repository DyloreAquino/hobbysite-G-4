# Generated by Django 5.1.5 on 2025-03-05 02:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default='No description available.')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default='No description available.')),
                ('price', models.DecimalField(decimal_places=2, max_digits=63)),
                ('product_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchstore.producttype')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
