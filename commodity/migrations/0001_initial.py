# Generated by Django 2.0.6 on 2020-05-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('CommodityNo', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter a commodity', max_length=200)),
            ],
        ),
    ]
