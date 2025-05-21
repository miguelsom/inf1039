from django.db import models
from django.conf import settings

class Profile(models.Model):
    USER_ROLES = [
        ("student", "Student"),
        ("teacher", "Teacher"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=10, choices=USER_ROLES, default="student")

    def is_student(self):
        return self.role == "student"

    def is_teacher(self):
        return self.role == "teacher"

    def __str__(self):
        return f'Profile of {self.user.username}'
