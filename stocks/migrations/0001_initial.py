# Generated by Django 2.0.6 on 2018-06-15 03:41

from django.db import migrations, models
import stocks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.IntegerField(default=stocks.models.Stocks.number, max_length=6, unique=True)),
                ('date', models.DateField()),
                ('Name', models.CharField(max_length=200)),
                ('commodity', models.CharField(max_length=200)),
                ('begs', models.IntegerField()),
                ('boxes', models.IntegerField()),
                ('remarks', models.TextField(max_length=200)),
            ],
        ),
    ]
