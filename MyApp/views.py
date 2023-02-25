from django.shortcuts import render

def index(request):
 return render(request,'index.html') 

def loan_application_form(request):
 return render(request,'loan_application_form.html') 


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