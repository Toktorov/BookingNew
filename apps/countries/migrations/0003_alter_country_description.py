# Generated by Django 3.2.7 on 2021-09-22 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_country_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Описание'),
        ),
    ]