# Generated by Django 4.2.5 on 2024-08-30 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_alter_club_officials_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='link',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
    ]
