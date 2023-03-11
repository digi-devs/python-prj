from django.db import models

# Create your models here.

class Department(models.Model):
    dep_id=models.AutoField(primary_key=True)
    dep_name=models.CharField(max_length=100)
    dep_loc=models.CharField(max_length=100)

    def __str__(self):
        return self.dep_name


class Roles(models.Model):
    role_id=models.AutoField(primary_key=True)
    role_name=models.CharField(max_length=100)

    def __str__(self):
        return self.role_name



class Employee(models.Model):
    emp_id=models.AutoField(primary_key=True)
    emp_fname=models.CharField(max_length=100,default='')
    emp_lname=models.CharField(max_length=100,default='')
    emp_dep=models.ForeignKey(Department, on_delete=models.CASCADE)
    emp_sal=models.IntegerField(default=0)
    emp_role=models.ForeignKey(Roles, on_delete=models.CASCADE)
    emp_phone=models.IntegerField(default=0)
    emp_hire_date=models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.emp_fname, self.emp_lname, self.emp_phone )

