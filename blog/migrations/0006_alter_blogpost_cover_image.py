# Generated by Django 4.2.7 on 2023-12-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='cover_image',
            field=models.ImageField(upload_to='post'),
        ),
    ]