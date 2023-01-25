from rest_framework import viewsets
from rest_framework.response import Response
from quiz_app.models import Quiz_Category, QuestionModel, General_Knowledge, Leaderboard, UserAndQuestion
from auth_app.models import User
from quiz_app.api.serializers import (QuizCategorySerializer, QuestionModelSerializer, 
                                    GeneralKnowledgeSerializer,
                                    QuestionAnswerSerializer, TakeQuizSerializer, LeaderboardSerializer)
from django.shortcuts import get_object_or_404
from rest_framework import status
from quiz_app.api.permissions import IsAdminOrReadOnly
from quiz_app.api.pagination import QuestionModelformVSPagination
from rest_framework import status, viewsets
import random
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


#Class For Quiz Category
class QuizCategoryformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        queryset = Quiz_Category.objects.all()
        serializer = QuizCategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Quiz_Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = QuizCategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        permission_classes = [IsAdminOrReadOnly]
        serializer = QuizCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk):
        queryset = Quiz_Category.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    def update(self, request, pk):
        queryset = Quiz_Category.objects.get(pk=pk)
        serializer = QuizCategorySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
#Class For Quiz Question
class QuestionModelformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def retrieve(self, request, pk=None):
        from rest_framework.pagination import PageNumberPagination
        queryset = QuestionModel.objects.filter(category=pk)
        paginator = QuestionModelformVSPagination()
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = QuestionModelSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = QuestionModelSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = QuestionModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk):
        queryset = QuestionModel.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = Quiz_Category.objects.get(pk=pk)
        serializer = QuestionModelSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Class For Quiz Leaderboard
class LeaderboardformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        queryset = Leaderboard.objects.all()
        serializer = LeaderboardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Leaderboard.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = QuestionModelSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data=request.data
        serializer = QuestionModelSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk):
        queryset = Leaderboard.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = Leaderboard.objects.get(pk=pk)
        serializer = QuestionModelSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
    
#Class For GeneralKnowledge
class GeneralKnowledgeformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        queryset = General_Knowledge.objects.all()
        today_topic = random.choice(queryset)
        serializer = GeneralKnowledgeSerializer(today_topic)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = General_Knowledge.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = QuestionModelSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = GeneralKnowledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
    def delete(self, request, pk):
        queryset = General_Knowledge.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        queryset = General_Knowledge.objects.get(pk=pk)
        serializer = GeneralKnowledgeSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#Class For Quiz Question and Answer
class QuestionAnswerformVS(viewsets.ViewSet):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def list(self, request):
        
        queryset = QuestionModel.objects.all()
        serializer = QuestionAnswerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        
        serializer = QuestionAnswerSerializer(data=request.data)
        if serializer.is_valid():        
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Class For Taking Quiz
class CreateAnswerVS(viewsets.ViewSet):
    
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['post'])
    def store_result(self, request):
        
        user_id = request.user
        quiz_id = request.data.get('quiz_id')
        question_id = request.data.get('question_id')
        answer = request.data.get('answer')
        
        # Check if user_id, quiz_id and question_id exists in the UserAndQuestion or not
        check_existence = UserAndQuestion.objects.filter(user_id=user_id, quiz_id=quiz_id, question_id=question_id)
        
        if not check_existence:
            # if user_id, quiz_id and question_id does not exists object is created
            model = UserAndQuestion()
            model.user_id = user_id
            model.question_id_id = question_id
            model.quiz_id_id = quiz_id
            model.save()
            
            # Filter the QuestionModel with passed question_id and answer
            check_answer = QuestionModel.objects.filter(id=question_id, answer=answer)

            try:
                result = Leaderboard.objects.get(user_name = user_id, quiz_name = quiz_id)
                
                if result.total == 10:
                    return Response({'message':'You have attended all ten questions'})
                
                else:
                    result.total += 1
                    
                    # Check for wrong answer
                    if not check_answer:
                        result.incorrect += 0.33
                        result.percentage = ((result.correct - result.incorrect)/result.total)*100
                        result.save()
                        
                    # Check for correct answer 
                    else:
                        result.correct += 1
                        result.percentage = ((result.correct - result.incorrect)/result.total)*100
                        result.save()
            
            # If Leaderboard does not exist with particular user_id and quiz_id then it is created
            except Leaderboard.DoesNotExist:
                result = Leaderboard()
                result.user_name = user_id
                result.quiz_name_id = quiz_id
                result.total += 1
                
                # Check for wrong answer
                if not check_answer:
                    result.incorrect += 0.33
                    result.percentage = ((result.correct - result.incorrect)/result.total)*100
                    result.save()

                # Check for correct answer 
                else:    
                    result.correct += 1
                    result.percentage = ((result.correct - result.incorrect)/result.total)*100
                    result.save()
                
            return Response({"your_answer":answer}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'You have attended this question'}, status=status.HTTP_400_BAD_REQUEST)
  