import datetime
import requests
from django.shortcuts import render
from books.models import Book  # Import your Book model

def home(request):
    year = datetime.datetime.now().year
    thought = "Keep learning, keep growing."

    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                thought = f"{data[0]['q']} — {data[0]['a']}"
    except Exception as e:
        print("Quote API Error:", e)

    # Fetch 3 random books from the database
    featured_books = Book.objects.order_by('?')[:3]

    context = {
        'thought': thought,
        'year': year,
        'featured_books': featured_books,
    }
    return render(request, 'core/home.html', context)
