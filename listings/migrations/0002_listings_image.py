# Generated by Django 4.2.3 on 2023-07-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='image',
            field=models.ImageField(default='', upload_to='media/'),
            preserve_default=False,
        ),
    ]