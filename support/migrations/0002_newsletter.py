# Generated by Django 4.2.6 on 2023-10-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
