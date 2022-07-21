from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pens/', views.pens_index, name='index'),
    path('pens/<int:pen_id>/', views.pens_detail, name='detail'),
]
