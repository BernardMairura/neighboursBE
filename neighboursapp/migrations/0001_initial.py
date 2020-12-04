# Generated by Django 3.1.4 on 2020-12-03 18:58

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HoodadminProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', tinymce.models.HTMLField(blank=True, max_length=100)),
                ('prof_picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hood_administrator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'adminprof',
            },
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=60)),
                ('hoodphoto', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('body', tinymce.models.HTMLField()),
                ('residents', models.IntegerField(blank=True, null=True)),
                ('emergency_contact', models.IntegerField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighborhood', to='neighboursapp.hoodadminprofile')),
            ],
            options={
                'db_table': 'neighborhood',
            },
        ),
        migrations.CreateModel(
            name='ResidentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=30)),
                ('bio', tinymce.models.HTMLField(blank=True, max_length=100)),
                ('prof_picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('contact', models.CharField(blank=True, max_length=15)),
                ('hoodname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home', to='neighboursapp.neighborhood')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbor_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('body', tinymce.models.HTMLField(blank=True)),
                ('location', models.CharField(max_length=60)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='neighboursapp.neighborhood')),
            ],
        ),
    ]
