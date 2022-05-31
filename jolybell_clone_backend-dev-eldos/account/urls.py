from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.UserProfileView.as_view()),
    path('profile/logout/', views.LogoutView.as_view()),
    path('profile/login/', views.LoginView.as_view()),
    path('profile/register/', views.RegisterView.as_view()),
]
