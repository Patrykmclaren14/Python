from re import search
from unicodedata import name
import requests


def get_authors(search: str = None):
    authors = []
    api_request = requests.get('https://wolnelektury.pl/api/authors/')
    api = api_request.json()
    for author_id, author in enumerate(api, start=1):
        if search is not None or search in author['name']:
            authors.append({
                'author_id': author_id,
                'author': author.get('name'),
                'api_books_url': author.get('href') + 'books'
            })
    return authors


authors = get_authors('Adam')
for author in authors:
    print(f'{author.get("author_id")}. {author.get("name")}')
query_id = int(input("Which book artist's want to see"))
found_author = filter(lambda x: x.get('author_id') == query_id, authors)
print(list(found_author))
