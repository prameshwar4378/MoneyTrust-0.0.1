# Generated by Django 4.1.7 on 2023-03-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_alter_db_loan_emp_type_alter_db_loan_salary_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_loan',
            name='salary_received',
            field=models.BigIntegerField(),
        ),
    ]
