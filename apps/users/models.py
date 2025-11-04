from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models
from apps.common.models import BaseModel


class User(AbstractUser, BaseModel):
    """User model for Admin, Student, Teacher roles"""
    USER_ROLES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]

    role = models.CharField(
        max_length=10, choices=USER_ROLES, default='student')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='profiles/', blank=True, null=True)
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # clash oldini olish
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # clash oldini olish
        blank=True,
    )

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_student(self):
        return self.role == 'student'

    @property
    def is_teacher(self):
        return self.role == 'teacher'