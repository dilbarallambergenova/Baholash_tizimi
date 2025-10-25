from django.db import models

from apps.users.models import User

class Group(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    QUESTION_TYPE_CHOICES=[
        ('test','Test'),
        ('file','File'),
        ('text','Text')
    ]
    title=models.CharField(max_length=250)
    question_type=models.CharField(max_length=10,choices=QUESTION_TYPE_CHOICES)
    content=models.TextField
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_questions')
    
    def __str__(self):
        return f"{self.title}" ({self.question_type})

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="answers")
    student=models.ForeignKey(User,on_delete=models.CASCADE,related_name="answers")
    text_answer=models.TextField(blank=True,null=True)
    file_answer=models.FileField(upload_to='answers/',blank=True,null=True)
    is_correct=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
         return f"Answer by {self.student.username} for {self.question.title}"
     
class Assignment(models.Model):
    ASSIGNMENT_TYPE_CHOICES = [
        ('exam', 'Exam'),
        ('homework', 'Homework'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assignment_type = models.CharField(max_length=10, choices=ASSIGNMENT_TYPE_CHOICES)
    questions = models.ManyToManyField(Question, related_name='assignments')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_assignments')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    deadline = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class TestSession(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_sessions')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='sessions')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}"


class Submission(models.Model):
    session = models.ForeignKey(TestSession, on_delete=models.CASCADE, related_name='submissions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.session.student.username}"
