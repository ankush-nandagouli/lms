from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


# ---------------------
# Utility Validators
# ---------------------
def validate_image_size(file):
    limit = 1 * 1024 * 1024  # 1 MB
    if file.size > limit:
        raise ValidationError('Image file too large. Max size is 1MB.')

def validate_pdf_size(file):
    limit = 5 * 1024 * 1024  # 5 MB
    if file.size > limit:
        raise ValidationError('PDF file too large. Max size is 5MB.')

# ---------------------
# Book Model
# ---------------------
class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('CSE', 'CSE'),
        ('ME', 'ME'),
        ('MI', 'MI'),
        ('CE', 'CE'),
        ('Math', 'Math'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')

    cover_image = models.ImageField(
        upload_to='book_covers/',
        blank=True,
        null=True,
        help_text="Upload JPG or PNG image",
        validators=[
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
            validate_image_size
        ]
    )

    pdf_file = models.FileField(
        upload_to='book_pdfs/',
        blank=True,
        null=True,
        help_text="Upload a PDF file",
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf']),
            validate_pdf_size
        ]
    )

    available = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} by {self.author}"
