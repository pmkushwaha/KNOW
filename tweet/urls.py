 
from django.urls import path
from .import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('user', views.user_profile,name='user_profile'),
     path('user/edit_profile', views.edit_profile,name='edit_profile'),
    path('tweet/', views.Tweet_list,name='Tweet_list'),
    path('create/', views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit,name='tweet_edit'), 
    path('<int:tweet_id>/delete/', views.tweet_delete,name='tweet_delete'), 
    path('register/', views.register,name='register'), 
 
    
] 