# Generated by Django 5.1.2 on 2025-03-17 22:55

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('party_date', models.DateField()),
                ('party_time', models.TimeField()),
                ('invitation', models.TextField()),
                ('venue', models.CharField(max_length=200)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'parties',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('attending', models.BooleanField(default=False)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='party.party')),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gift', models.CharField(max_length=200)),
                ('price', models.FloatField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='party.party')),
            ],
        ),
    ]
