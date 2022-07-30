from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('bins/', views.bins_index, name='index'),
    path('bins/<int:bin_id>/', views.bins_detail, name='detail'),
    path('bins/create/', views.BinCreate.as_view(), name='bins_create'),
    path('bins/<int:pk>/update/', views.BinUpdate.as_view(), name='bins_update'),
    path('bins/<int:pk>/delete/', views.BinDelete.as_view(), name='bins_delete'),
    path('bins/<int:bin_id>/add_pen/', views.add_pen, name='add_pen'),
    path('bins/<int:bin_id>/assoc_label/<int:label_id>/', views.assoc_label, name='assoc_label'),
    path('labels/', views.LabelList.as_view(), name='labels_index'),
    path('labels/<int:pk>/', views.LabelDetail.as_view(), name='labels_detail'),
    path('labels/create/', views.LabelCreate.as_view(), name='labels_create'),
    path('labels/<int:pk>/update/', views.LabelUpdate.as_view(), name='labels_update'),
    path('labels/<int:pk>/delete/', views.LabelDelete.as_view(), name='labels_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
