from django.urls import path
from . import views

# URL Configuration
urlpatterns = [
    path('', views.render_homepage),
    path('robots/', views.display_robots),
]