# Generated by Django 4.0.6 on 2022-07-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('last_logged_in', models.DateField(auto_now_add=True)),
            ],
        ),
    ]