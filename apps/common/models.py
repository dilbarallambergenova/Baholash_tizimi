from django.db import models
from users.models import User
from assignments.models import Assignment

class Result(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    graded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}: {self.score}"


class Appeal(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='appeals')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Appeal by {self.student.username}"

