# Generated by Django 4.2.2 on 2023-07-25 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='user_type',
            field=models.CharField(choices=[('SPONSOR', 'SPONSOR'), ('VOLUNTEER', 'VOLUNTEER'), ('MEMBER', 'MEMBER')], max_length=9),
        ),
    ]
