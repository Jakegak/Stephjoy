from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def students(request):
    return render(request, 'students/students.html')


def newstudent(request):
    return render(request, 'students/edit_student.html')


def editstudent(request):
    return render(request, 'students/new_student.html')