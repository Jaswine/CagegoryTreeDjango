# Generated by Django 3.2.12 on 2024-04-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='treecategory',
            name='named_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
