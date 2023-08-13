from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    data = [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date,
            'description': book.description,
            'page_count': book.page_count,
            'categories': book.categories,
            'thumbnail_url': book.thumbnail_url,
        }
        for book in books
    ]
    
    return JsonResponse({'books': data})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    data ={
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'published_date': book.published_date,
            'description': book.description,
            'page_count': book.page_count,
            'categories': book.categories,
            'thumbnail_url': book.thumbnail_url,
            }
    
    return JsonResponse(data)

@csrf_exempt
def create_book(request):
    if request.method == 'POST':
        data = request.POST
        new_book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            published_date=data['published_date'],
            description=data['description'],
            page_count=data['page_count'],
            categories=data['categories'],
            thumbnail_url=data.get('thumbnail_url', ''),
        )
        return JsonResponse({
            'message': 'Book created successfully!',
            'book': {
                'id': new_book.id,
                'title': new_book.title,
                'author': new_book.author,
                'published_date': new_book.published_date,
                'description': new_book.description,
                'page_count': new_book.page_count,
                'categories': new_book.categories,
                'thumbnail_url': new_book.thumbnail_url,
            }
        })
    else:
        return JsonResponse({'message': 'Invalid request method'})