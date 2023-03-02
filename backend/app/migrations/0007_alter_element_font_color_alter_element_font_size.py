# Generated by Django 4.1.5 on 2023-03-02 15:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_textelement_alter_element_font_size_delete_selector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='font_color',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='element',
            name='font_size',
            field=models.PositiveIntegerField(blank=True, default=10, null=True, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(128)]),
        ),
    ]
