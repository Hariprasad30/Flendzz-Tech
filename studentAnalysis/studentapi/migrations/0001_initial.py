# Generated by Django 3.1.14 on 2022-01-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_list_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('rollNumber', models.CharField(max_length=3)),
                ('marks', models.CharField(max_length=100)),
            ],
        ),
    ]