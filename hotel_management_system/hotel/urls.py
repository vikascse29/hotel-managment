from django.contrib import admin
from django.urls import path
from hotel import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('rooms/', views.room_list, name='room_list'),
    path('reservation/', views.make_reservation, name='make_reservation'),
    path('reservation/success/', views.reservation_success, name='reservation_success'),
    path('staff/', views.staff_list, name='staff_list'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
]