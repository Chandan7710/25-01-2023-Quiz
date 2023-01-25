from rest_framework import serializers
from quiz_app.models import Quiz_Category, QuestionModel, General_Knowledge, Leaderboard

# serializer for Quiz Questions
class QuestionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        exclude = ('answer',)

# serializer for Quiz Category    
class QuizCategorySerializer(serializers.ModelSerializer):
    
    category = QuestionModelSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz_Category
        fields = "__all__"
      
# serializer for Quiz Leaderboard  
class LeaderboardSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Leaderboard
        fields = "__all__"

# serializer for Daily GeneralKnowledge    
class GeneralKnowledgeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = General_Knowledge
        fields = "__all__"

# serializer to Display Quiz Question and Answer   
class QuestionAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = QuestionModel
        fields = ['id', 'question', 'answer', 'category']

# serializer to Take Quiz And Pass The Answers
class TakeQuizSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    answer = serializers.CharField(max_length=200)