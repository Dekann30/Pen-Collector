from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pens/', views.pens_index, name='index'),
    path('pens/<int:pen_id>/', views.pens_detail, name='detail'),
    path('pens/create/', views.PenCreate.as_view(), name='pens_create'),
    path('pens/<int:pk>/update/', views.PenUpdate.as_view(), name='pens_update'),
    path('pens/<int:pk>/delete/', views.PenDelete.as_view(), name='pens_delete'),
]
