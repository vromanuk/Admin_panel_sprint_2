# Generated by Django 3.2.4 on 2021-06-15 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="birth_date",
            field=models.DateField(null=True),
        ),
    ]