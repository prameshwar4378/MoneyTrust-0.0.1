from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import login_form
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import Form_Loan_Application,Form_Become_Partner,Form_Enquiry
from .filters import Loan_Application_Records_Filter,Become_Partner_Records_Filter,Enquiry_Filter
from django.core.paginator import Paginator
from .models import DB_Loan,DB_Become_Partner,DB_Enquiry
from django.http import HttpResponse
import csv

def test(request):
 return render(request,'test.html') 

def index(request):
 return render(request,'index.html') 

def admin_login(request):
    form=login_form()
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user) 
            return redirect('/admin_dashboard',{'user',user})
        else:
            form=login_form()
            messages.error(request,'Opps...! User does not exist... Please try again..!')
    return render(request,"admin/admin_login.html",{'form':form})

def admin_logout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/admin_login')
def admin_dashboard(request):
    loan_aplication_count=DB_Loan.objects.count()
    become_partner_count=DB_Become_Partner.objects.count()
    enquiry_count=DB_Enquiry.objects.count()
    data={'loan_aplication_count':loan_aplication_count,'become_partner_count':become_partner_count,'enquiry_count':enquiry_count}
    return render(request,'admin/admin_dashboard.html',data) 

def enquiry_records(request):
    rec=DB_Enquiry.objects.order_by('-id')
    Filter=Enquiry_Filter(request.GET, queryset=rec)
    rec2=Filter.qs 
    count=rec2.count()
    paginator=Paginator(rec2,10)
    page_number=request.GET.get('page')
    page_record_finel=paginator.get_page(page_number)
 
    totalpage=page_record_finel.paginator.num_pages
    data={'rec':page_record_finel,'filter':Filter,'count':count,'pagenumbers':[n+1 for n in range(totalpage)]} 
    return render(request,'admin/enquiry_records.html',data)
 


def delete_enquiry(request,id):
    if request.method=='POST':
        rm=DB_Enquiry.objects.get(pk=id)
        rm.delete()
        messages.success(request,'Record Deleted Successfully')
    return redirect('/enquiry_records/',{'rm':rm})
   

def enquiry_records_more_details(request,id):
    rec=DB_Enquiry.objects.get(pk=id)
    return render(request,'admin/enquiry_records_more_details.html',{'rec':rec})
   


def loan_application_records(request):
    rec=DB_Loan.objects.order_by('-id')
    Filter=Loan_Application_Records_Filter(request.GET, queryset=rec)
    rec2=Filter.qs 
    count=rec2.count()
    paginator=Paginator(rec2,10)
    page_number=request.GET.get('page')
    page_record_finel=paginator.get_page(page_number)
 
    totalpage=page_record_finel.paginator.num_pages
    data={'rec':page_record_finel,'filter':Filter,'count':count,'pagenumbers':[n+1 for n in range(totalpage)]} 
    return render(request,'admin/loan_application_records.html',data)


def delete_loan_application_record(request,id):
    if request.method=='POST':
        rm=DB_Loan.objects.get(pk=id)
        rm.delete()
        messages.success(request,'Record Deleted Successfully')
    return redirect('/loan_application_records/',{'rm':rm})




def become_a_partner_records(request):
    rec=DB_Become_Partner.objects.order_by('-id')
    Filter=Become_Partner_Records_Filter(request.GET, queryset=rec)
    rec2=Filter.qs 
    count=rec2.count()
    paginator=Paginator(rec2,10)
    page_number=request.GET.get('page')
    page_record_finel=paginator.get_page(page_number)
 
    totalpage=page_record_finel.paginator.num_pages
    data={'rec':page_record_finel,'filter':Filter,'count':count,'pagenumbers':[n+1 for n in range(totalpage)]} 
    return render(request,'admin/become_a_partner_records.html',data)


def delete_become_partner(request,id):
    if request.method=='POST':
        rm=DB_Become_Partner.objects.get(pk=id)
        rm.delete()
        messages.success(request,'Record Deleted Successfully')
    return redirect('/become_a_partner_records/',{'rm':rm})


def export_data_become_partner(request):
    
    responce=HttpResponse(content_type='text/csv')
    writer=csv.writer(responce)
    writer.writerow(['First Name','Last Name','Mobile','Email','City','Profession','Pan',"Application Date"])
    for data in DB_Become_Partner.objects.all().values_list('first_name','last_name','mobile','email','city','profession','pan','date_time' ):
       writer.writerow(data)
    
    # return redirect('/become_a_partner_records/')
    responce['Content-Disposition'] = 'attachment; filename="Become a Partner.csv"'
    return responce




def export_data_enquiry(request):
    
    responce=HttpResponse(content_type='text/csv')
    writer=csv.writer(responce)
    writer.writerow(['First Name','Last Name','Mobile','Email','City','Reason','Subject',"Message"])
    for data in DB_Enquiry.objects.all().values_list('first_name','last_name','mobile','email','city','reason','subject','message' ):
       writer.writerow(data)
    
    # return redirect('/become_a_partner_records/')
    responce['Content-Disposition'] = 'attachment; filename="Enquiry.csv"'
    return responce




def export_data_loan_application(request):
    
    responce=HttpResponse(content_type='text/csv')
    writer=csv.writer(responce)
    writer.writerow(['First Name','Last Name','Pin Code','Mobile','Income','Imployee Type','Loan Amount','Salary Received',"Application Date"])
    for data in DB_Loan.objects.all().values_list('first_name','last_name','pin_code','mobile','income','emp_type','loan_amount','salary_received','date_time' ):
       writer.writerow(data)
    
    # return redirect('/become_a_partner_records/')
    responce['Content-Disposition'] = 'attachment; filename="Loan Application.csv"'
    return responce






def loan_application_form(request):
    fm=Form_Loan_Application()
    if request.method=="POST":
        
        fm=Form_Loan_Application(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thank You')
            return redirect('/')
    return render(request,'loan_application_form.html',{'fm':fm})


 

def contact_us(request):
    fm=Form_Enquiry()
    if request.method=="POST":
        fm=Form_Enquiry(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thank You')
            return redirect('/')
    return render(request,'contact_us.html',{'fm':fm}) 



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
    fm=Form_Become_Partner()
    if request.method=="POST":
        fm=Form_Become_Partner(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thank You')
            # return redirect('/')
    return render(request,'become_partner.html',{'fm':fm})

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


# Home Loan Start 

def car_loan_overview(request):
 return render(request,'car_loan_overview.html')

def car_loan_eligibility_criteria(request):
 return render(request,'car_loan_eligibility_criteria.html')

def car_loan_document_required(request):
 return render(request,'car_loan_document_required.html')

# Home Loan Start 

 