# Generated by Django 5.0 on 2024-03-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.TextField(default='hdhdhd'),
            preserve_default=False,
        ),
    ]