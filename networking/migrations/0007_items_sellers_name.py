# Generated by Django 4.2.5 on 2024-08-12 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networking', '0006_items_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='sellers_name',
            field=models.CharField(default='8Tech', max_length=100),
        ),
    ]
