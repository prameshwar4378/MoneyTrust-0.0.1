# Generated by Django 4.1.7 on 2023-03-06 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_alter_db_loan_emp_type_alter_db_loan_salary_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_loan',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='db_loan',
            name='income',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='db_loan',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='db_loan',
            name='loan_amount',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='db_loan',
            name='mobile',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='db_loan',
            name='pin_code',
            field=models.BigIntegerField(null=True),
        ),
    ]
