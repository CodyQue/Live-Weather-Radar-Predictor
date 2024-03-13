# Generated by Django 4.2.11 on 2024-03-13 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=20)),
                ('temperature', models.CharField(max_length=20)),
                ('wind', models.CharField(max_length=20)),
                ('humidity', models.CharField(max_length=20)),
            ],
        ),
    ]
