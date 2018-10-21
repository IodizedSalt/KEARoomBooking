# Generated by Django 2.1.1 on 2018-10-13 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Campus', '0004_auto_20181011_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floorNumber', models.CharField(max_length=2)),
                ('roomNumber', models.CharField(max_length=5)),
                ('roomID', models.CharField(max_length=10)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Campus.Campus')),
            ],
        ),
    ]