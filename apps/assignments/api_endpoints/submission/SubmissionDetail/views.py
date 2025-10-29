from rest_framework import generics,permissions
from apps.assignments.api_endpoints.submission.SubmissionDetail.serializers import SubmissionDetailSerializer
from apps.assignments.models import Submission

class SubmissionDetailView(generics.RetrieveAPIView):
    serializer_class=SubmissionDetailSerializer
    permission_classes=[permissions.IsAuthenticated]
    queryset=Submission.objects.all()
    
    
    def get_queryset(self):
        user=self.request.user
        if user.role=='student':
            return Submission.objects.filter(student=user)
        elif user.role=='teacher':
            return Submission.objects.filter(assigment_teacher=user)
        elif user.role=='admin':
            return Submission.objects.all()
        return Submission.objects.none()