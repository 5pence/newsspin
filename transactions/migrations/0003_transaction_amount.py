# Generated by Django 2.1 on 2018-08-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_auto_20180807_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
