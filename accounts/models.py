from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid
from django.conf import settings

def generate_library_id():
    """Generate a unique library card ID"""
    return f"LMS-{uuid.uuid4().hex[:8].upper()}"


class CustomUser(AbstractUser):
    # Role field with choices for better clarity and extensibility
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('librarian', 'Librarian'),
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='student',  # Default role for new users
    )

    is_approved = models.BooleanField(default=False, help_text="Admin approval required before login")


    # Auto-generated unique library card ID
    library_card = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default=generate_library_id,
        unique=True,
        help_text="Auto-generated unique library card ID"
    )

    # Profile picture for students
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        help_text="Student's profile image"
    )

    # Additional Student Profile Info
    branch = models.CharField(max_length=100, blank=True, null=True)
    roll_number = models.CharField(max_length=20, blank=True, null=True)
    academic_session = models.CharField(max_length=20, blank=True, null=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)

    # Avoid conflicts with auth.User reverse relationships
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

    def is_student(self):
        return self.role == 'student'

    def is_teacher(self):
        return self.role == 'teacher'

    def is_librarian(self):
        return self.role == 'librarian'

class StudentRegistration(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f"Student Registration: {self.full_name}"


class TeacherRegistration(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"Teacher Registration: {self.full_name}"