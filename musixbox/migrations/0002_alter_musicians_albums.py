# Generated by Django 3.2.4 on 2021-06-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musixbox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicians',
            name='albums',
            field=models.ManyToManyField(blank=True, to='musixbox.MusicAlbums'),
        ),
    ]
