
from django.urls import path
from . import views

urlpatterns = [
    path('', views.addshow, name='studentform'),
    path('edit/<int:id>/', views.editstd, name='editstudent'),
    path('deletestudent/<int:id>/', views.delete_std, name='deletestudent'),
    # path('addshow/', views.addshow,{}),
]
