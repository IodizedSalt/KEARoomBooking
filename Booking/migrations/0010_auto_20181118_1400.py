# Generated by Django 2.1.1 on 2018-11-18 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0009_auto_20181118_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='emailID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]