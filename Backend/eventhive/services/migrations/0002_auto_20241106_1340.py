# Generated by Django 5.1.3 on 2024-11-06 08:10

from django.db import migrations


def create_initial_categories(apps, schema_editor):
    ServiceCategory = apps.get_model('services', 'ServiceCategory')
    initial_categories = [
        {"name": "Venues", "description": "Event venues and spaces"},
        {"name": "Catering", "description": "Food and beverage catering services"},
        {"name": "Photography", "description": "Photography and videography services"},
        {"name": "Entertainment", "description": "Entertainment services such as DJs, bands, etc."},
        {"name": "Event Planners", "description": "Event planning and coordination services"},
        {"name": "Sports", "description": "Sports event services and ticketing"},
        {"name": "Concerts and Shows", "description": "Concerts, shows, and live performances"},
        {"name": "Hotels", "description": "Hotel accommodation services"}
    ]
    
    for category in initial_categories:
        ServiceCategory.objects.get_or_create(**category)


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_categories),
    ]