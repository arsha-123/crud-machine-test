from django.shortcuts import render
from admin_app.models import Student


# Create your views here.
def admin_login(request):
    return render(request,'adminapp/admin_login.html')



def dashboard(request):
    return render(request,'adminapp/dashboard.html')


def register(request):
    if request.method=='POST':
        a_name=request.POST['b_name']
        a_contact=request.POST['b_contact']
        a_email=request.POST['b_email']
        a_username=request.POST['b_username']
        a_password=request.POST['b_password']
       
        fac_obj=Student(name=a_name,contact=a_contact,email=a_email,username=a_username,password=a_password)
        fac_obj.save()
    return render(request,'adminapp/register.html')



def active(request):
    return render(request,'adminapp/active.html')



