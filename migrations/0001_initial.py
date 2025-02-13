# Generated by Django 3.1.1 on 2020-09-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idsubject', models.CharField(max_length=5)),
                ('subject', models.CharField(max_length=64)),
                ('term', models.PositiveIntegerField()),
                ('year', models.CharField(max_length=4)),
                ('seat', models.PositiveIntegerField(default=3)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
