# Generated by Django 5.1.3 on 2024-11-06 09:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20241106_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Catering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catering_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('available_locations', models.CharField(max_length=200)),
                ('price_weekday', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_weekend', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact', models.CharField(max_length=15)),
                ('cuisine_type', models.CharField(blank=True, max_length=100, null=True)),
                ('minimum_order_size', models.PositiveIntegerField()),
                ('photos', models.JSONField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caterings', to='services.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='ConcertAndShow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location_name', models.CharField(max_length=100)),
                ('location_map', models.URLField(blank=True, null=True)),
                ('ticket_type', models.JSONField()),
                ('price_by_ticket', models.JSONField()),
                ('available_tickets_for_each_type', models.JSONField()),
                ('performer_name', models.CharField(max_length=200)),
                ('event_date', models.DateField()),
                ('duration', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='concert_and_shows', to='services.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Entertainment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('available_locations', models.CharField(max_length=200)),
                ('price_weekday', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_weekend', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact', models.CharField(max_length=15)),
                ('performance_duration', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entertainments', to='services.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='EventPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('available_locations', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('event_type', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_planners', to='services.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location_name', models.CharField(max_length=100)),
                ('location_map', models.URLField(blank=True, null=True)),
                ('room_type', models.JSONField()),
                ('price_by_room_type', models.JSONField()),
                ('available_rooms_for_each_type', models.JSONField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='services.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='PhotographyVideography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('available_locations', models.CharField(max_length=200)),
                ('price_weekday', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_weekend', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact', models.CharField(max_length=15)),
                ('service_duration', models.DecimalField(decimal_places=2, max_digits=5)),
                ('photos', models.JSONField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photography_videographies', to='services.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location_name', models.CharField(max_length=100)),
                ('location_map', models.URLField(blank=True, null=True)),
                ('price_by_seating', models.JSONField()),
                ('event_date', models.DateField()),
                ('seating_map_url', models.URLField(blank=True, null=True)),
                ('ticket_type', models.JSONField()),
                ('available_tickets_for_each_type', models.JSONField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sports', to='services.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('location_name', models.CharField(max_length=100)),
                ('location_map', models.URLField(blank=True, null=True)),
                ('price_weekday', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_weekend', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact_phone', models.CharField(max_length=15)),
                ('capacity', models.PositiveIntegerField()),
                ('facilities', models.JSONField(blank=True, null=True)),
                ('event_type_compatibility', models.JSONField(blank=True, null=True)),
                ('photos', models.JSONField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venues', to='services.servicecategory')),
            ],
        ),
    ]
