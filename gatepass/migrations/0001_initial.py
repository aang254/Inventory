# Generated by Django 2.0.6 on 2018-06-22 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stocks', '0006_auto_20180619_0959'),
        ('commodity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='gate_pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passNo', models.IntegerField(unique=True)),
                ('date', models.DateField()),
                ('driver_name', models.CharField(max_length=30, null=True)),
                ('Auto_No', models.CharField(max_length=20, null=True)),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.TextField(max_length=200, null=True)),
                ('gstin', models.CharField(max_length=15, verbose_name='GSTIN')),
                ('bill_no', models.CharField(max_length=40)),
                ('bags', models.IntegerField()),
                ('boxes', models.IntegerField()),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.Commodity')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Stocks')),
            ],
        ),
    ]