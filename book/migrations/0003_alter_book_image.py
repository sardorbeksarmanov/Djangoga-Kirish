# Generated by Django 5.0.6 on 2024-07-06 17:26

import book.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(null=True, upload_to=book.helpers.SaveMedia.save_book_image_path),
        ),
    ]
