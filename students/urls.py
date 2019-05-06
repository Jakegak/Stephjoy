from django.urls import path
import students.views

urlpatterns = [
    path('', students.views.students, name='students'),
    path('new_student', students.views.newstudent, name='newStud'),
    path('edit_student', students.views.editstudent, name='editStud'),
    path('<int:student_id>', students.views.details, name='details'),
]
