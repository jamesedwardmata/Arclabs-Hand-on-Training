# Generated by Django 4.1.7 on 2023-04-12 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0004_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
