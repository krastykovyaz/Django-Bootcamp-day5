# Generated by Django 3.2.2 on 2021-05-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('episode_nb', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, unique=True)),
                ('opening_crawl', models.TextField(null=True)),
                ('director', models.CharField(max_length=32)),
                ('producer', models.CharField(max_length=128)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
