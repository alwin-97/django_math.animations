# Generated by Django 2.2.7 on 2020-02-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fossee_math_pages', '0010_data_data_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='data_image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='data',
            name='data_video',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]