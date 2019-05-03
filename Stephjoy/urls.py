from django.contrib import admin
from django.urls import path, include
import students.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', students.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),
]
