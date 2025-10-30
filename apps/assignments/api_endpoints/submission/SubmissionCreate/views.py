from rest_framework import generics,permissions

from apps.assignments.api_endpoints.submission.SubmissionCreate.serializers import SubmissionCreateSerializer



class SubmissionCreateView(generics.CreateAPIView):
    serializer_class=SubmissionCreateSerializer
    permission_classes=[permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

