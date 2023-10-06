# Generated by Django 4.2.2 on 2023-10-05 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userprofile_interests_userprofile_mobile_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('date_of_birth', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=20)),
                ('whatsapp_number', models.CharField(max_length=20)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]