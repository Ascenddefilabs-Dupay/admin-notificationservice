# Generated by Django 5.1 on 2024-10-01 09:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminProductAnnouncement',
            fields=[
                ('content_id', models.CharField(editable=False, max_length=6, primary_key=True, serialize=False, unique=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.localtime)),
            ],
            options={
                'db_table': 'admin_product_announcement',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductAnnouncementNotifications',
            fields=[
                ('notification_id', models.CharField(editable=False, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('user_id', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'product_announcement_notifications',
            },
        ),
    ]