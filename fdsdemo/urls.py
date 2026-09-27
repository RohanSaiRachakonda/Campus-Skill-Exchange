from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('profile/', views.profile, name='profile'),
    path('explore/', views.explore_skills, name='explore_skills'),
    path('logout/', views.logout_view, name='logout'),
]