# Generated by Django 4.1.7 on 2023-03-08 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_alter_db_become_partner_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_become_partner',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='db_become_partner',
            name='profession',
            field=models.CharField(choices=[('Chartered Accountant', 'Chartered Accountant'), ('Finincial Analyst', 'Finincial Analyst'), ('Freelancer', 'Freelancer'), ('Builder', 'Builder'), ('Ex.Banker', 'Ex.Banker')], max_length=200),
        ),
    ]
