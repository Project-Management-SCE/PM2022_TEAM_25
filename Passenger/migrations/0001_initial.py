# Generated by Django 4.0.4 on 2022-04-12 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='passengers',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('fn', models.CharField(max_length=20)),
                ('ln', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=14)),
                ('gender', models.CharField(default='male', max_length=5)),
                ('age', models.SmallIntegerField()),
            ],
        ),
    ]
