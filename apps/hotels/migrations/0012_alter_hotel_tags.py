# Generated by Django 3.2.7 on 2021-09-28 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_remove_tag_hotels'),
        ('hotels', '0011_alter_hotel_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='hotel_tags', to='tags.Tag'),
        ),
    ]