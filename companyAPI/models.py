from django.db import models

# Create your models here.
class CompanyModel(models.Model):
    types = (('IT','IT'),('Service','Service'))
    company_id=models.AutoField(primary_key=True)
    comapny_name=models.CharField(max_length=500)
    company_location=models.CharField(max_length=300)
    company_about=models.CharField(max_length=300)
    company_type=models.CharField(max_length=400,choices=types)
    added_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=False)