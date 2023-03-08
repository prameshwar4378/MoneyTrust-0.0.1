from django.db import models
 

EMP_TYPE=(
    ('Salaried','Salaried'),
    ('Self-employed','Self-employed'),
    ('Business Owner','Business Owner'),
    ('Other','Other'),
)

SALARY_RECEIVED=(
    ('Bank Transfer','Bank Transfer'),
    ('Cash','Cash'),
    ('Chaque','Chaque'),
)
class DB_Loan(models.Model):
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    pin_code=models.BigIntegerField(null=True)
    mobile=models.CharField(max_length=200,null=True)
    income=models.IntegerField(null=True)
    emp_type=models.CharField(max_length=50,null=True,choices=EMP_TYPE)
    loan_amount=models.BigIntegerField(null=True)
    salary_received=models.CharField(max_length=50,null=True,choices=SALARY_RECEIVED)
    date_time=models.DateTimeField(auto_now=True, auto_now_add=False,editable=True)




CITY=(
    ('Chh.Sambhajinagar','Chh.Sambhajinagar'),
    ('Pune','Pune'),
    ('Nashik','Nashik'),
    ('Mumbai','Mumbai'),
    ('Nagpur','Nagpur'),
    ('Latur','Latur'),
)
PROFESSION={
    ('Builder','Builder'),
    ('Chartered Accountant','Chartered Accountant'),
    ('Ex.Banker','Ex.Banker'),
    ('Finincial Analyst','Finincial Analyst'),
    ('Freelancer','Freelancer'),

}
class DB_Become_Partner(models.Model):
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    mobile=models.CharField(max_length=200,null=True)
    email=models.EmailField( max_length=254)
    city=models.CharField( max_length=200,choices=CITY)
    profession=models.CharField(max_length=200,choices=PROFESSION)
    pan=models.CharField(max_length=50)
    date_time=models.DateTimeField(auto_now=True, auto_now_add=False,editable=True)



REASON={
    ('Complaints Related','Complaints Related'), 
    ('Communication Address','Communication Address'), 
    ('Document Issue','Document Issue'), 
    ('Other','Other') 
}

class DB_Enquiry(models.Model):
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    mobile=models.CharField(max_length=200,null=True)
    email=models.EmailField( max_length=254)
    city=models.CharField( max_length=200,choices=CITY)
    reason=models.CharField( max_length=200,choices=REASON)
    subject=models.CharField( max_length=400)
    message=models.TextField(max_length=1000)
    


