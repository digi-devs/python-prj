from django.urls import path
from EmpAPI import views


urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.create, name='create'),
    path('read/',views.read, name='read'),
    path('getUpdate/',views.getUpdate, name='getUpdate'),
    path('update/<int:emp_id>',views.update, name='update'),
    path('delete/',views.delete, name='delete'),
    path('filter/',views.filter, name='filter'),
    path('delete/<int:emp_id>',views.delete, name='delete'),
    
]
