from django.urls import path
from .views import (
     register, login_user, logout_user, profile, profile_update,
    librarian_dashboard, approve_user, reject_user, export_users_csv,
    registered_students, registered_teachers,
    teacher_dashboard, suspend_student,
    librarian_login, teacher_login, pending_approvals, student_register, teacher_register, student_profile_view, student_management, view_student_profile, toggle_suspend_student
)
from django.contrib.auth import views as auth_views
urlpatterns = [
    # 🔵 General user actions
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('register/student/', student_register, name='student_register'),
    path('register/teacher/', teacher_register, name='teacher_register'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    path('student-profile/<int:user_id>/', student_profile_view, name='student_profile'),


    # 🔵 Librarian section
    path('librarian/login/', librarian_login, name='librarian_login'),
    path('librarian/dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('librarian/approve/<int:user_id>/', approve_user, name='approve_user'),
    path('librarian/pending-approvals', pending_approvals, name='pending_approvals'),
    path('librarian/reject/<int:user_id>/', reject_user, name='reject_user'),
    path('librarian/export/', export_users_csv, name='export_users_csv'),
    path('librarian/registered-students/', registered_students, name='registered_students'),
    path('librarian/registered-teachers/', registered_teachers, name='registered_teachers'),
    path('librarian/students/', student_management, name='student_management'),
    path('librarian/students/<int:student_id>/', view_student_profile, name='view_student_profile'),
    path('librarian/students/<int:student_id>/toggle-suspend/', toggle_suspend_student, name='toggle_suspend_student'),

    # 🔵 Teacher section
    path('teacher/login/', teacher_login, name='teacher_login'),
    path('teacher/dashboard/', teacher_dashboard, name='teacher_dashboard'),
    path('teacher/suspend/<int:user_id>/', suspend_student, name='suspend_student'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
