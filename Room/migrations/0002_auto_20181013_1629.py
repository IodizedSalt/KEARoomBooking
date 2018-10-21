# Generated by Django 2.1.1 on 2018-10-13 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=3)),
                ('whiteboard', models.BooleanField(default=False)),
                ('projector', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='roomID',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AddField(
            model_name='roomdetails',
            name='roomDetailsID',
            field=models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='Room.Room', to_field='roomID'),
        ),
    ]