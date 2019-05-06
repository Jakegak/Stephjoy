from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student

def home(request):
    return render(request, 'home.html')

Students = Student.objects.all()
@login_required
def students(request):
    return render(request, 'students/students.html', {'Students':Students})

@login_required
def newstudent(request):
    if request.method == 'POST':
        if request.POST['first_name'] and request.POST['second_name'] and request.POST['last_name'] and request.POST['classes'] and request.POST['phone_number'] and request.FILES['photo'] and request.POST['admin_number']:
            student = Student()
            student.admin_number = request.POST['admin_number']
            student.first_name = request.POST['first_name']
            student.second_name = request.POST['second_name']
            student.last_name = request.POST['last_name']
            student.classes = request.POST['classes']
            student.phone_number = request.POST['phone_number']
            student.fingerPrint = 'None'
            student.photo = request.FILES['photo']
            student.save()
            return redirect('students')
        else:
            return render(request, 'students/new_student.html', {'errors': 'Make sure you have filled all the required fields'})

    else:
        return render(request, 'students/new_student.html')


@login_required
def editstudent(request):
    return render(request, 'students/edit_student.html')

@login_required
def details(request, student_id):
    studDetails = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/studDetails.html', {'stud':studDetails})