# Generated by Django 4.0 on 2021-12-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField(max_length=200)),
                ('ename', models.CharField(max_length=200)),
                ('eemail', models.CharField(max_length=100)),
                ('econtact', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.DeleteModel(
            name='students',
        ),
    ]
