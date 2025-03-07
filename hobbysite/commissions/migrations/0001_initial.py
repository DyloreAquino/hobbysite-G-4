# Generated by Django 5.1.6 on 2025-03-05 04:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('requiredPeople', models.IntegerField()),
                ('createdOn', models.DateTimeField()),
                ('updatedOn', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField()),
                ('createdOn', models.DateTimeField()),
                ('updatedOn', models.DateTimeField()),
                ('commission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commission', to='commissions.commission')),
            ],
        ),
    ]
