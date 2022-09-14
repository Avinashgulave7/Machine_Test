from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Login,name='login'),
    path("home/",views.Index,name='index'),
    path("add/",views.Add_Book,name='add_book'),
    path('delete/<int:id>/',views.Book_Delete,name='deletebook'),
    path('update/<int:id>/',views.Book_Update,name='updatebook'),
    path('signup/',views.Sign_Up,name='singup')

    ]