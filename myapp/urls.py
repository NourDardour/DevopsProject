from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/<int:pk>/', views.company_detail, name='company_detail'),
    path('recruiters/', views.recruiter_list, name='recruiter_list'),
    path('recruiters/<int:pk>/', views.recruiter_detail, name='recruiter_detail'),
    path('reviews/<str:review_type>/<int:pk>/add/', views.add_review, name='add_review'),
    path('reviews/<int:pk>/delete/', views.delete_review, name='delete_review'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('search/', views.search, name='search'),
]

