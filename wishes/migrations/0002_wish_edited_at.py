# Generated by Django 5.1.7 on 2025-03-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='edited_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
