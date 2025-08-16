from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'category',
            'description',
            'available',
            'cover_image',
            'pdf_file',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter a brief summary'}),
            'title': forms.TextInput(attrs={'placeholder': 'Book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author name'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_cover_image(self):
        image = self.cleaned_data.get('cover_image')
        if image and image.size > 1 * 1024 * 1024:  # 1 MB limit
            raise forms.ValidationError("Cover image size should not exceed 1 MB.")
        return image

    def clean_pdf_file(self):
        pdf = self.cleaned_data.get('pdf_file')
        if pdf and pdf.size > 5 * 1024 * 1024:  # 5 MB limit
            raise forms.ValidationError("PDF file size should not exceed 5 MB.")
        return pdf
