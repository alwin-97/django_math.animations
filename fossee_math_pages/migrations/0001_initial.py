# Generated by Django 2.2.7 on 2020-01-14 03:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_content', models.TextField()),
                ('data_reference', models.TextField(blank=True)),
                ('data_post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('data_status', models.CharField(choices=[('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED'), ('WAITING', 'WAITING'), ('UNDER REVIEW', 'UNDER REVIEW')], default='WAITING', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship_topic', models.CharField(max_length=255)),
                ('internship_thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('internship_start_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('internship_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('COMPLETED', 'COMPLETED')], default='INACTIVE', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', phonenumber_field.modelfields.PhoneNumberField(default='+91', max_length=128, region=None, unique=True)),
                ('user_role', models.CharField(choices=[('INTERN', 'INTERN'), ('STAFF', 'STAFF')], default='INTERN', max_length=20)),
                ('user_temp_password', models.CharField(blank=True, max_length=10)),
                ('user_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], default='INACTIVE', max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=255)),
                ('internship_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossee_math_pages.Internship')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subtopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtopic_name', models.CharField(max_length=255)),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossee_math_pages.Topic')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossee_math_pages.Internship')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DataVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataverification_verifier', models.CharField(max_length=255)),
                ('dataverification_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('data_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossee_math_pages.Data')),
                ('dataverification_mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='data',
            name='subtopic_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossee_math_pages.Subtopic'),
        ),
        migrations.AddField(
            model_name='data',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_message', models.TextField()),
                ('chat_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('internship_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fossee_math_pages.Internship')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
