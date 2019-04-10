# Generated by Django 2.2 on 2019-04-09 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ReservaBarberia', '0005_auto_20190409_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='codbarbero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReservaBarberia.Barbero'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='codclie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ReservaBarberia.Cliente'),
        ),
    ]