# Generated by Django 4.0.2 on 2022-02-21 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('display_name', models.CharField(max_length=200)),
                ('brief_bio', models.CharField(max_length=255, verbose_name='Brief bio')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(auto_now=True)),
                ('source', models.TextField()),
                ('ip_address', models.CharField(max_length=30)),
                ('misc_headers', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Submissions',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('source', models.CharField(max_length=400)),
                ('slug', models.SlugField(unique=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.author')),
                ('categories', models.ManyToManyField(to='quotes.Categories')),
            ],
        ),
    ]