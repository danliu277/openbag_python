# Generated by Django 3.0.8 on 2020-08-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('game_id', models.IntegerField()),
                ('employee_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
