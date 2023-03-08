# Generated by Django 4.1.7 on 2023-03-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0011_db_enquiry_alter_db_become_partner_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_become_partner',
            name='profession',
            field=models.CharField(choices=[('Ex.Banker', 'Ex.Banker'), ('Chartered Accountant', 'Chartered Accountant'), ('Finincial Analyst', 'Finincial Analyst'), ('Builder', 'Builder'), ('Freelancer', 'Freelancer')], max_length=200),
        ),
        migrations.AlterField(
            model_name='db_enquiry',
            name='reason',
            field=models.CharField(choices=[('Document Issue', 'Document Issue'), ('Complaints Related', 'Complaints Related'), ('Communication Address', 'Communication Address'), ('Other', 'Other')], max_length=200),
        ),
    ]
