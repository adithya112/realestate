# Generated by Django 4.2.3 on 2023-07-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('num_bed', models.IntegerField()),
                ('num_bath', models.IntegerField()),
                ('sq_foot', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
