import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books_project.settings')
django.setup()

import requests
from books.models import Book

def populate_books():
    search_terms = 'stormlight archive'
    api_url = f'https://www.googleapis.com/books/v1/volumes?q={search_terms}'

    try:
        response = requests.get(api_url)
        data = response.json()

        for item in data.get('items', []):
            volume_info = item.get('volumeInfo', {})
            Book.objects.create(
                title=volume_info.get('title', 'No Title'),
                author=', '.join(volume_info.get('authors', [])),
                published_date=volume_info.get('publishedDate', ''),
                description=volume_info.get('description', ''),
                page_count=volume_info.get('pageCount', 0),
                categories=', '.join(volume_info.get('categories', [])),
                thumbnail_url=volume_info.get('imageLinks', {}).get('thumbnail', ''),
            )
            print(f"Created book: {volume_info.get('title')}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    populate_books()
