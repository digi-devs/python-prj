from django.shortcuts import render
from EmpAPI.models import Employee
from datetime import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        emp_fname = request.POST['emp_fname']
        emp_lname = request.POST['emp_lname']
        emp_dep = int(request.POST['emp_dep'])
        emp_sal = int(request.POST['emp_sal'])
        emp_role = int(request.POST['emp_role'])
        emp_phone = int(request.POST['emp_phone'])

        new_emp = Employee(emp_fname = emp_fname, 
                           emp_lname = emp_lname, 
                           emp_dep_id = emp_dep, 
                           emp_sal = emp_sal, 
                           emp_role_id = emp_role, 
                           emp_phone = emp_phone,  
                           emp_hire_date = datetime.now()
                           )
        new_emp.save()
        msg = {'msg':'Employee Added'}
        return render(request, 'msg.html',msg)
    else:
        return render(request, 'create.html')

def read(request,emp_id = 0):
    all_emp = Employee.objects.all()
    context = {
        'all_emp':all_emp,
    }
    return render(request, 'read.html',context)

def getUpdate(request):
    all_emp = Employee.objects.all()
    context = {
        'all_emp':all_emp
    }
    return render(request, 'getUpdate.html',context)

def update(request,emp_id):
    if request.method == 'POST':
        try:
            emp = Employee.objects.get(emp_id=emp_id)
            emp.emp_fname = request.POST['emp_fname']
            emp.emp_lname = request.POST['emp_lname']
            emp.emp_dep_id = int(request.POST['emp_dep'])
            emp.emp_sal = int(request.POST['emp_sal'])
            emp.emp_role_id = int(request.POST['emp_role'])
            emp.emp_phone = int(request.POST['emp_phone'])

            emp.save()
            print('Msg ============== ')
            msg = {'msg':'Employee Update Success'}
            return render(request, 'msg.html',msg)
        except:
            msg = {'msg':'Employee Update Failed'}
            return render(request, 'msg.html',msg)
    else:
        get_emp = Employee.objects.get(emp_id=emp_id)
        context= {
            'get_emp':get_emp
        }
        return render(request, 'update.html',context)
    

def filter(request):
    if request.method == 'POST':
        emp_name = request.POST['emp_name']
        emp_dep = request.POST['emp_dep']
        emp_role = request.POST['emp_role']
        all_emp = Employee.objects.all()
        if emp_name:
            all_emp = all_emp.filter(Q(emp_fname__icontains = emp_name) | Q(emp_lname__icontains = emp_name))
        if emp_dep:
            all_emp = all_emp.filter(emp_dep__dep_name__icontains = emp_dep)
        if emp_role:
            all_emp = all_emp.filter(emp_role__role_name__icontains = emp_role)
        
        context = {
            'all_emp':all_emp
        }
        return render(request, 'read.html',context)
    return render(request, 'filter.html')

def delete(request,emp_id=0):
    if emp_id:
        try:
            get_emp = Employee.objects.get(emp_id=emp_id)
            get_emp.delete()
            msg = {'msg':'Employee Deleted'}
            return render(request, 'msg.html',msg)
        except:
            msg = {'msg':'Something Went Wrong'}
            return render(request, 'msg.html',msg) 
    all_emp = Employee.objects.all()
    context = {
        'all_emp':all_emp,
        }
    return render(request, 'delete.html',context)
    