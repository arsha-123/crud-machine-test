from django.shortcuts import render,redirect
from admin_app.models import Student

# Create your views here.

def student_login(request):
    error=''
    if request.method == 'POST':
        user_name = request.POST['f_email']
        std_password = request.POST['f_password']
        seller_data = Student.objects.filter(
            username=user_name, password=std_password).exists()
        if seller_data:
            seller=Student.objects.get(username=user_name,password=std_password)
            request.session['student_id']=seller.id
            return redirect('update')
        else:
            error = "Invalid user name and password"

    return render(request,'student_app/student_login.html',{'error':error})



# def update(request):
#     return render(request,'student_app/update.html')


def update(request):
    student_name= request.session['student_id']
    student_display=Student.objects.get(id=student_name)
    return render(request,'student_app/update.html',{'stu':student_display})     

