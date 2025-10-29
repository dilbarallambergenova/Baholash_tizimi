
from rest_framework import serializers
from apps import assignments
from apps.assignments.models import Submission

class SubmissionDetailSerializer(serializers.ModelSerializer):
    student_name=serializers.SerializerMethodField()
    assignment_title=serializers.CharField(source='assignment.title',read_only=True)
    
    
    class Meta:
        model=Submission
        fields=[
            'id','student_name','assignment_title',
            'status','total_score','percentage_score',
            'is_passed','started_at','submitted_at','time_spent_minutes'
        ]
        
    def get_student_name(self,obj):
        return obj.student.get_full_name()