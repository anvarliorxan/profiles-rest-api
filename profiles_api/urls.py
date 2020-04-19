from django.urls import path
from profiles_api import views

urlpatterns = [
    path('view/',views.ApiView.as_view()),
    ]
