# Generated by Django 4.2 on 2023-10-23 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_student_record_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='website.student_record')),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=2)),
                ('bangla', models.IntegerField()),
                ('english', models.IntegerField()),
                ('math', models.IntegerField()),
                ('physics', models.IntegerField()),
                ('biology', models.IntegerField()),
                ('chemistry', models.IntegerField()),
            ],
        ),
    ]
