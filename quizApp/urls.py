from django.urls import path
from . import views

app_name = 'quizApp'

urlpatterns = [
    path('', views.quiz_list, name="quiz_list"),
    path('<int:quiz_id>/', views.take_quiz, name="take_quiz"),
    path('<int:quiz_id>/result/', views.quiz_result, name="quiz_result"),  # Different path for results
]