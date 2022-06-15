from django.urls import path,include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    
    path('login/',views.signin,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.signout,name='logout'),
   
   
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit'),
    path('project/<post>', views.project, name='project'),
    path('search/', views.search_project, name='search'),
    path('api/post/',views.PostList.as_view()),
    path('api/profile/', views.ProfileList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)