# Generated by Django 5.0.6 on 2024-06-06 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf', models.IntegerField()),
                ('rack', models.IntegerField()),
                ('cell', models.IntegerField()),
                ('cell_code', models.CharField(max_length=100)),
                ('fill_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('receive_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=255)),
                ('inventory_number', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('arrival_date', models.DateField()),
                ('issue_dates', models.JSONField(default=list)),
                ('cell_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.archive')),
            ],
        ),
    ]