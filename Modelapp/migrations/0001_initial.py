# Generated by Django 3.2.24 on 2024-02-27 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=20)),
                ('Lastname', models.CharField(max_length=20)),
                ('emailaddress', models.EmailField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('Age', models.IntegerField()),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
