# Generated by Django 4.1.7 on 2023-03-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_loan',
            name='emp_type',
            field=models.CharField(choices=[('Vaijapur', 'Vaijapur'), ('Gangapur', 'Gangapur')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='db_loan',
            name='salary_received',
            field=models.BigIntegerField(choices=[('Vaijapur', 'Vaijapur'), ('Gangapur', 'Gangapur')]),
        ),
    ]