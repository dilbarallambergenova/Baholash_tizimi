from ast import Sub
from re import sub
from rest_framework import serializers

from apps.assignments.models import Submission


class SubmissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Submission
        fields=[
            'assigment','test_session','status',
            'time_spent_minutse','total_score'
        ]
    
    
    def create(self,validated_data):
        user=self.context['request'].user
        submission=Submission.objects.create(student=user,**validated_data)
        return submission