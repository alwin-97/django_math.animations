# Generated by Django 2.2.7 on 2019-12-11 17:46

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('topic', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='+91', max_length=128, region=None, unique=True)),
                ('role', models.CharField(choices=[('INTERN', 'Intern'), ('STAFF', 'Staff')], default='INTERN', max_length=20)),
                ('joined_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('temp_password', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE'), ('SUSPENDED', 'SUSPENDED')], default='INACTIVE', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=False)),
                ('subtopic', models.CharField(max_length=255)),
                ('text', ckeditor.fields.RichTextField()),
                ('post_date', models.DateTimeField(default=datetime.datetime(2019, 12, 11, 23, 16, 2, 565070))),
                ('aproval_ststus', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AddUserView',
            fields=[
                ('adduser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fossee_math_pages.AddUser')),
            ],
            bases=('fossee_math_pages.adduser',),
        ),
    ]
