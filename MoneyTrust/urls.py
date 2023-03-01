"""MoneyTrust URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('', views.index, name="index"),
    path('become_partner/', views.become_partner, name="become_partner"),

    # Personal Loan Start 
    path('personal_loan_overview/', views.personal_loan_overview, name="personal_loan_overview"),
    path('personal_loan_eligibility_criteria/', views.personal_loan_eligibility_criteria, name="personal_loan_eligibility_criteria"),
    path('personal_loan_document_required/', views.personal_loan_document_required, name="personal_loan_document_required"),
    path('personal_loan_interest_rate_and_fees/', views.personal_loan_interest_rate_and_fees, name="personal_loan_interest_rate_and_fees"),
    path('loan_application_form/', views.loan_application_form, name="loan_application_form"),
    # Personal Loan Stop

    # Business Loan Start 
    path('business_loan_overview/', views.business_loan_overview, name="business_loan_overview"),
    path('business_loan_eligibility_criteria/', views.business_loan_eligibility_criteria, name="business_loan_eligibility_criteria"),
    path('business_loan_document_required/', views.business_loan_document_required, name="business_loan_document_required"),
    path('business_loan_interest_rate_and_fees/', views.business_loan_interest_rate_and_fees, name="business_loan_interest_rate_and_fees"),
    # Business Loan Stop

    # Doctor Loan Start 
    path('doctor_loan_overview/', views.doctor_loan_overview, name="doctor_loan_overview"),
    path('doctor_loan_eligibility_criteria/', views.doctor_loan_eligibility_criteria, name="doctor_loan_eligibility_criteria"),
    path('doctor_loan_document_required/', views.doctor_loan_document_required, name="doctor_loan_document_required"),
    path('doctor_loan_interest_rate_and_fees/', views.doctor_loan_interest_rate_and_fees, name="doctor_loan_interest_rate_and_fees"),
    # Doctor Loan Stop

    # Home Loan Start 
    path('home_loan_overview/', views.home_loan_overview, name="home_loan_overview"), 
    path('home_loan_eligibility_criteria/', views.home_loan_eligibility_criteria, name="home_loan_eligibility_criteria"),
    path('home_loan_document_required/', views.home_loan_document_required, name="home_loan_document_required"),
    path('home_loan_interest_rate_and_fees/', views.home_loan_interest_rate_and_fees, name="home_loan_interest_rate_and_fees"),
    # Home Loan Stop

]
