from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateCandidate.as_view()),
    path('<int:candidate_id>/', views.CandidateView.as_view()),
]
