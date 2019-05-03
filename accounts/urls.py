from django.urls import path
import accounts.views

urlpatterns = [
    path('login/', accounts.views.login_user, name = 'login'),
    path('',  accounts.views.signup, name = 'signup'),
    path('logout/', accounts.views.logout_user, name = 'logout'),
]
