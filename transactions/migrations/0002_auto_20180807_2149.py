# Generated by Django 2.1 on 2018-08-07 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transactions', '0001_initial'),
        ('users', '0001_initial'),
        ('tickets', '0002_ticket_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.User'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tickets.Ticket'),
        ),
    ]