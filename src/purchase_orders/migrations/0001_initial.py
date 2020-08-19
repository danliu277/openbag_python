# Generated by Django 3.0.8 on 2020-08-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.IntegerField()),
                ('employee_id', models.IntegerField()),
                ('vendor_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]