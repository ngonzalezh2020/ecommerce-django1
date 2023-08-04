# Generated by Django 4.2.3 on 2023-07-16 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('cat_image', models.ImageField(blank=True, upload_to='photo/categories')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
