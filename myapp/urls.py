from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:company_id>/', views.company_detail, name='company_detail'),
    path('companies/add/', views.add_company, name='add_company'),
    path('companies/<int:company_id>/add_review/', views.add_review, name='add_review'),
    path('recruiters/', views.recruiter_list, name='recruiter_list'),
    path('recruiters/<int:recruiter_id>/', views.recruiter_detail, name='recruiter_detail'),
    path('recruiters/add/', views.add_recruiter, name='add_recruiter'),
    path('recruiters/<int:recruiter_id>/add_review/', views.add_recruiter_review, name='add_recruiter_review'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
]
