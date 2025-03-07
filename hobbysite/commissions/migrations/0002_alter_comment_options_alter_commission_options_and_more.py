# Generated by Django 5.1.5 on 2025-03-07 12:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-createdOn']},
        ),
        migrations.AlterModelOptions(
            name='commission',
            options={'ordering': ['-createdOn']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='commission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='commissions.commission'),
        ),
    ]
