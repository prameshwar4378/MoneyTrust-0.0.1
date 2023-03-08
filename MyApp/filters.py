import django_filters
from django import forms
from .models import DB_Loan,DB_Become_Partner,DB_Enquiry
from django_filters import DateFilter


class Loan_Application_Records_Filter(django_filters.FilterSet):
    start_date=DateFilter(field_name='date_time',lookup_expr='gte')
    end_date=DateFilter(field_name='date_time',lookup_expr='lte')

    def __init__(self, *args, **kwargs):
        super(Loan_Application_Records_Filter, self).__init__(*args, **kwargs)
        self.filters['start_date'].label="Start Date - MM/DD/YYYY"
        self.filters['end_date'].label="End Date - MM/DD/YYYY"

    class Meta:
        model = DB_Loan
        fields = ['first_name','emp_type']

 
    

class Become_Partner_Records_Filter(django_filters.FilterSet):
    start_date=DateFilter(field_name='date_time',lookup_expr='gte')
    end_date=DateFilter(field_name='date_time',lookup_expr='lte')

    def __init__(self, *args, **kwargs):
        super(Become_Partner_Records_Filter, self).__init__(*args, **kwargs)
        self.filters['start_date'].label="Start Date - MM/DD/YYYY"
        self.filters['end_date'].label="End Date - MM/DD/YYYY"

    class Meta:
        model = DB_Become_Partner
        fields = ['city','profession']

 
        

class Enquiry_Filter(django_filters.FilterSet):
    start_date=DateFilter(field_name='date_time',lookup_expr='gte')
    end_date=DateFilter(field_name='date_time',lookup_expr='lte')

    def __init__(self, *args, **kwargs):
        super(Enquiry_Filter, self).__init__(*args, **kwargs)
        self.filters['start_date'].label="Start Date - MM/DD/YYYY"
        self.filters['end_date'].label="End Date - MM/DD/YYYY"

    class Meta:
        model = DB_Enquiry
        fields = ['city']

 
    