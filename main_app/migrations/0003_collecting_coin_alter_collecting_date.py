# Generated by Django 4.1 on 2022-08-10 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_collecting'),
    ]

    operations = [
        migrations.AddField(
            model_name='collecting',
            name='coin',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.coin'),
        ),
        migrations.AlterField(
            model_name='collecting',
            name='date',
            field=models.DateField(verbose_name='Collection date'),
        ),
    ]