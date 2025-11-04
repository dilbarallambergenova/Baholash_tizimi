from django.urls import path
from apps.assignments.api_endpoints.submission.SubmissionList.views import SubmissionListView

urlpatterns = [
    path('submissions/',SubmissionListView.as_view(),name='submission-list'),
]
