# Generated by Django 4.2.3 on 2023-07-13 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='recipe_ingredients',
            new_name='recipe_ingredient',
        ),
    ]
