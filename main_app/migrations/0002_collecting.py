# Generated by Django 4.1 on 2022-08-09 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collecting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.IntegerField()),
                ('prospecting', models.CharField(choices=[('M', 'Morning'), ('N', 'Noon'), ('E', 'Evening')], default='M', max_length=1)),
            ],
        ),
    ]
