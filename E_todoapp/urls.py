from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name ='home'),
    path('edit', views.edit,name ='edit'),
    path('index', views.index,name ='index'),
    path('login', views.log,name ='login'),
    path('profile', views.profile,name ='profile'),
    path('signup', views.sign,name ='signup'),
    path('add_task', views.add_task,name ='add_task'),
    path('delete', views.delete,name ='delete'),
    path('update', views.update,name ='update'),
]