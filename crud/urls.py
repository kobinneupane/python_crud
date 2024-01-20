from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    ##get data
    path('add-student/',postStudent),
    path('add-teacher/',postTeacher),
    
    ##fetch data
    path("get-student/",getStudent),
    path("get-teacher/",getTeacher),
    
    ##edit data
    path("edit-student/<id>",editStudent),
    path("update-student/<id>",updateStudentData),
    
    ##delete data
    path("delete-student/<id>",deleteStudentData)
]