# Generated by Django 4.2.6 on 2023-10-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='changed_by_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feedback',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
