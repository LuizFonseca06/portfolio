# Generated by Django 4.2.3 on 2024-01-08 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description_text',
            field=models.TextField(default=''),
        ),
    ]
