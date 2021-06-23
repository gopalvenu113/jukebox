# Generated by Django 3.2.4 on 2021-06-23 12:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicAlbums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)])),
                ('date_of_release', models.DateTimeField(auto_now_add=True)),
                ('genre', models.CharField(choices=[(1, 'Instrumental'), (2, 'Classical'), (3, 'POP'), (4, 'Rock'), (5, 'Western')], max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(1000)])),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Musicians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)])),
                ('musician_type', models.CharField(max_length=20, null=True)),
                ('albums', models.ManyToManyField(blank=True, null=True, to='musixbox.MusicAlbums')),
            ],
        ),
    ]
