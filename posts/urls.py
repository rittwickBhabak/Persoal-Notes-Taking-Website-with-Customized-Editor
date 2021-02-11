from django.urls import path, include
from posts import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('addnew', views.addnew, name='addnew'),
    path('details/<int:pk>', views.postdetails, name='postdetails'),
    path('deletepost/<int:pk>', views.postdelete, name='postdelete'),
    path('update/<int:pk>', views.postupdate, name='postupdate'),
    path('addtag/', views.addtag, name='addtag'),
    path('category/<str:cat>', views.category, name='category'),
    path('search/', views.search, name='search'),
]  