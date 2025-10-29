from rest_framework import generics,permissions
from apps.assignments.api_endpoints.submission.SubmissionList.serializers import SubmissionListSerializer
from apps.assignments.models import Submission


class SubmissionListView(generics.ListAPIView):
    serializer_class=SubmissionListSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def get_queryset(self):
        user=self.request.user
        
        if user.role=='student':
            return Submission.objects.filter(student=user)
        elif user.role=='teacher':
            return Submission.objects.filter(assignment_teacher=user)
        elif user.role=='admin':
            return Submission.objects.all()
        return Submission.objects.none()