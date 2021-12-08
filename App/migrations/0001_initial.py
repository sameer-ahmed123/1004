# Generated by Django 4.0 on 2021-12-08 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_roll', models.IntegerField(max_length=200)),
                ('student_class', models.IntegerField(max_length=20)),
            ],
            options={
                'db_table': 'student_details',
            },
        ),
    ]
