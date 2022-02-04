from django.urls import path
from . import views


urlpatterns = [
    path('<int:skill_id>', views.SkillDetailsView.as_view()),
    path('active/', views.ActiveSkillsView.as_view()),
]
