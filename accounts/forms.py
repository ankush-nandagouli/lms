from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, StudentRegistration, TeacherRegistration

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['full_name', 'email', 'mobile_number', 'course', 'year_of_study', 'address']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input w-full border-blue-500 rounded-md'}),
            'email': forms.EmailInput(attrs={'class': 'form-input w-full border-gray-300 rounded-md'}),
            'mobile_number': forms.TextInput(attrs={'class': 'form-input w-full border-gray-300 rounded-md'}),
            'course': forms.TextInput(attrs={'class': 'form-input w-full border-gray-300 rounded-md'}),
            'year_of_study': forms.TextInput(attrs={'class': 'form-input w-full border-gray-300 rounded-md'}),
            'address': forms.Textarea(attrs={'class': 'form-textarea w-full border-gray-300 rounded-md', 'rows': 3}),
        }

class TeacherRegisterForm(forms.ModelForm):
    class Meta:
        model = TeacherRegistration
        fields = ['full_name', 'email', 'mobile_number', 'designation', 'department', 'address']



# 👤 Profile Update Form (for student dashboard)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'profile_picture',
            'branch',
            'roll_number',
            'academic_session',
            'mobile_number'
        ]
        widgets = {
            'branch': forms.TextInput(attrs={'placeholder': 'e.g. Computer Science'}),
            'roll_number': forms.TextInput(attrs={'placeholder': 'e.g. CS21045'}),
            'academic_session': forms.TextInput(attrs={'placeholder': 'e.g. 2021-2025'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'e.g. 0000000000'}),
        }


# 🛠 Admin Update Form (optional, useful if customizing admin)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
