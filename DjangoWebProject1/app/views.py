"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from .forms import MyForm
from django.template import loader
from app.models import Employee


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def department_list(request):

     all_data = Employee.objects.filter(department__startswith='Testing')
    
     return render(
        request,
        'app/department_list.html',
        {
            'title':'List',
            'message':'Your Data list description page.',
            'year':datetime.now().year,
            'Employee': all_data
        }
    
    )

def human_department(request):

     all_data = Employee.objects.filter(department__startswith='Human Resource')
    
     return render(
        request,
        'app/human_department.html',
        {
            'title':'human_department',
            'message':'Your Data list description page.',
            'year':datetime.now().year,
            'Employee': all_data
        }
    
    )

def new_department(request):

     all_data = Employee.objects.filter(department__startswith='1234')
    
     return render(
        request,
        'app/new_department.html',
        {
            'title':'new_department',
            'message':'Your Data list description page.',
            'year':datetime.now().year,
            'Employee': all_data
        }
    
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
def list(request):
    #Select*from Where...
    # all_data = Employee.objects.filter(department__startswith='Testing')
    all_data = Employee.objects.all()
    
    return render(
        request,
        'app/list.html',
        {
            'title':'List',
            'message':'Your Data list description page.',
            'year':datetime.now().year,
            'Employee': all_data
        }
    
    )


def contact(request):
 #if form is submitted  
     print("contact")
     print(request.method)
     if request.method == 'POST':
        print("post")

        myForm = MyForm(request.POST)

        if myForm.is_valid():
            print("valid")
            name = myForm.cleaned_data['name']
            lname = myForm.cleaned_data['lname']
            department = myForm.cleaned_data['department']
            age = myForm.cleaned_data['age']
            birthdate = myForm.cleaned_data['birthdate']
   
            


            context = {
            'name': name,
            'lname': lname,
            'department': department,
            'age': age,
            'birthdate' : birthdate,
           
            }

            template = loader.get_template('app/about.html')

            #returing the template
            e = Employee(name=name,lname=lname,department=department,age=age,birthdate=birthdate)
            e.save()
            return HttpResponse(template.render(context, request))
     else:
         form = MyForm()
     #returning form

     return render(request, 'app/contact.html',  {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
            'form':form});
