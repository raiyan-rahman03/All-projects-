# Generated by Django 4.2 on 2023-10-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('roll_no', models.IntegerField()),
                ('grade_level', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField(max_length=40)),
                ('address', models.CharField(max_length=150)),
                ('class_room_no', models.CharField(max_length=10)),
            ],
        ),
    ]