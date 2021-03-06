# Generated by Django 4.0.3 on 2022-04-08 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=64)),
                ('country', models.CharField(blank=True, max_length=64)),
                ('region', models.CharField(blank=True, max_length=64)),
                ('post_code', models.CharField(blank=True, max_length=64)),
                ('city', models.CharField(blank=True, max_length=64)),
                ('address', models.CharField(blank=True, max_length=128)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
