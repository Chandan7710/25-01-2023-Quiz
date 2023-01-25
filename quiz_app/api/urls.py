from rest_framework.routers import DefaultRouter
from quiz_app.api.views import (QuizCategoryformVS, QuestionModelformVS, 
                                GeneralKnowledgeformVS,
                                QuestionAnswerformVS, CreateAnswerVS, LeaderboardformVS)

from django.urls import path, include

router = DefaultRouter()

router.register('quizcategory', QuizCategoryformVS, basename = 'quizcategory')
router.register('quiz_question', QuestionModelformVS, basename = 'quizquestionone')
router.register('leaderboard', LeaderboardformVS, basename = 'leaderboard')
router.register('generalknowledge', GeneralKnowledgeformVS, basename = 'generalknowledge')
router.register('questionanswer', QuestionAnswerformVS, basename = 'questionanswer')
router.register('takequiz', CreateAnswerVS, basename = 'takequiz')

urlpatterns = [
    
    path('', include(router.urls)),
    
]
