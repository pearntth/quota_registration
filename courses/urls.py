from django.urls import path

from . import views

urlpatterns = [
    path('course_list/', views.register, name='course_list'),
    path('request_quota/<int:course_id>/', views.request_quota, name='request_quota'),
    path('cancel_request/<int:course_id>/', views.cancel_request, name='cancel_request'),
]