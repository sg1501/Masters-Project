"""Hospital_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index, name='home'),
    path('add_doctor', Add_Doctor, name='add_doctor'),
    path('add_patient', Add_Patient, name='add_patient'),
    path('add_appointment', Add_Appointment, name='add_appointment'),
    path('view_doctor', view_Doctor, name='view_doctor'),
    path('view_appointment', view_Appointment, name='view_appointment'),
    path('view_patient', view_Patient, name='view_patient'),
    path('delete_doctor/(?P<pid>[0-9]+)', Delete_Doctor, name='delete_doctor'),
    path('delete_appointment/(?P<pid>[0-9]+)', Delete_Appointment, name='delete_appointment'),
    path('delete_patient/(?P<pid>[0-9]+)', Delete_Patient, name='delete_patient'),
    path('edit_patient/(?P<pid>[0-9]+)', Edit_Patient, name='edit_patient'),
    path('edit_doctor/(?P<pid>[0-9]+)', Edit_Doctor, name='edit_doctor'),
    path('admin_login', Login, name='login'),
    path('logout', Logout_admin, name='logout')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
