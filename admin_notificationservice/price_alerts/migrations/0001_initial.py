# Generated by Django 5.1 on 2024-10-07 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminManageCryptoCurrencies',
            fields=[
                ('currency_id', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True)),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('coin_gecko_id', models.CharField(max_length=50, unique=True)),
                ('price_change_threshold', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'admin_manage_crypto_currencies',
            },
        ),
        migrations.CreateModel(
            name='PriceAlertsNotifications',
            fields=[
                ('notification_id', models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('user_id', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'price_alerts_notifications',
            },
        ),
        migrations.CreateModel(
            name='AdminPriceAlerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('price_inr', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price_alerts.adminmanagecryptocurrencies')),
            ],
            options={
                'db_table': 'admin_price_alerts',
            },
        ),
    ]