# Generated by Django 3.2.17 on 2023-07-16 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]