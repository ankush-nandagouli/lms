from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q


def browse_books(request):
    books = Book.objects.filter(available=True).order_by('-uploaded_at')  # Filter only available books

    query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')

    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))
    if category_filter:
        books = books.filter(category=category_filter)

    paginator = Paginator(books, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Book.CATEGORY_CHOICES

    return render(request, 'books/browse_books.html', {
        'page_obj': page_obj,
        'query': query,
        'category_filter': category_filter,
        'categories': categories
    })


def is_librarian(user):
    return user.is_authenticated and user.is_librarian

@login_required
@user_passes_test(is_librarian)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            if book.available is None:
                book.available = True  # fallback safety
            book.save()
            messages.success(request, "✅ Book added successfully!")
            return redirect('browse_books')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})