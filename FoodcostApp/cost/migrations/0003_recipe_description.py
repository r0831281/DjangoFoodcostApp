# Generated by Django 4.2.3 on 2023-07-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0002_rename_recipe_ingredients_recipe_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='empty'),
            preserve_default=False,
        ),
    ]