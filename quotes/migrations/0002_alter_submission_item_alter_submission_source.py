# Generated by Django 4.1.7 on 2023-03-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="item",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="submission",
            name="source",
            field=models.CharField(max_length=400),
        ),
    ]