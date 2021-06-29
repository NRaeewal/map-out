from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('vacations/', views.vacations_index, name='index'),
    path('vacations/<int:vacation_id>/', views.vacations_detail, name='detail'),
    path('vacations/<int:pk>/delete/', views.VacationDelete.as_view(), name='vacations_delete'),
]