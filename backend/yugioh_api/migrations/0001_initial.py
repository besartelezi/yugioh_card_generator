# Generated by Django 4.2 on 2023-04-29 13:25

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MonsterCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('attribute', models.CharField(max_length=90)),
                ('stars', models.PositiveIntegerField(default=4, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('type', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), size=None)),
                ('description', models.CharField(max_length=250)),
                ('attack', models.PositiveBigIntegerField()),
                ('defense', models.PositiveIntegerField()),
            ],
        ),
    ]