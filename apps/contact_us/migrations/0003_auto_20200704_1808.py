# Generated by Django 2.2.11 on 2020-07-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_auto_20200704_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rastamember',
            name='photo_hidden',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
