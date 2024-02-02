from django.contrib import admin
from django.urls import path,include
from app import views



urlpatterns = [
    path('student/',views.StudentList.as_view()),
]

