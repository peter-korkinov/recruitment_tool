from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecruitersView.as_view()),
]
