from django.contrib import admin
from django.urls import path, include
import students.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', students.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
