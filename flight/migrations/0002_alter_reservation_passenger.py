# Generated by Django 4.2.1 on 2023-08-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='passenger',
            field=models.ManyToManyField(blank=True, to='flight.passenger'),
        ),
    ]
