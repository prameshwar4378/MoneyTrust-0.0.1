from django.shortcuts import render

def test(request):
 return render(request,'test.html') 

def index(request):
 return render(request,'index.html') 

def loan_application_form(request):
 return render(request,'loan_application_form.html') 

# Personal Loan Start 

def personal_loan_overview(request):
 return render(request,'personal_loan_overview.html')

def personal_loan_eligibility_criteria(request):
 return render(request,'personal_loan_eligibility_criteria.html')

def personal_loan_interest_rate_and_fees(request):
 return render(request,'personal_loan_interest_rate_and_fees.html')

def personal_loan_document_required(request):
 return render(request,'personal_loan_document_required.html')

def become_partner(request):
 return render(request,'become_partner.html')

# Stop Loan Start 


# Business Loan Start 

def business_loan_overview(request):
 return render(request,'business_loan_overview.html')

def business_loan_eligibility_criteria(request):
 return render(request,'business_loan_eligibility_criteria.html')

def business_loan_interest_rate_and_fees(request):
 return render(request,'business_loan_interest_rate_and_fees.html')

def business_loan_document_required(request):
 return render(request,'business_loan_document_required.html')

# Business Loan Start 


# Doctor Loan Start 

def doctor_loan_overview(request):
 return render(request,'doctor_loan_overview.html')

def doctor_loan_eligibility_criteria(request):
 return render(request,'doctor_loan_eligibility_criteria.html')

def doctor_loan_interest_rate_and_fees(request):
 return render(request,'doctor_loan_interest_rate_and_fees.html')

def doctor_loan_document_required(request):
 return render(request,'doctor_loan_document_required.html')

# Doctor Loan Start 




# Home Loan Start 

def home_loan_overview(request):
 return render(request,'home_loan_overview.html')

def home_loan_eligibility_criteria(request):
 return render(request,'home_loan_eligibility_criteria.html')

def home_loan_interest_rate_and_fees(request):
 return render(request,'home_loan_interest_rate_and_fees.html')

def home_loan_document_required(request):
 return render(request,'home_loan_document_required.html')

# Home Loan Start 