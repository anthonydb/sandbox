# from django.core.mail import mail_admins
import requests
from datetime import datetime
from .keys import *


def fetch_nyt_booklist(list_type):
    # Construct API url
    api_key = nyt_api
    base_url = 'https://api.nytimes.com/svc/books/v3/lists/current/'
    url = f"{base_url}{list_type}.json?api-key={api_key}"

    # Attempt to fetch the API and build a list of titles
    try:
        r = requests.get(url)
        nyt_list_response = r.json()
        nyt_api_list_date_string = nyt_list_response['results']['bestsellers_date']
        nyt_list_date = datetime.strptime(nyt_api_list_date_string, '%Y-%m-%d').strftime('%m/%d/%Y')

        # A list of dicts for titles
        top_list = []

        for book in nyt_list_response['results']['books']:
            books_dict = {
                    'rank': str(book['rank']),
                    'rank_lw': '-' if book['rank_last_week'] == 0 else str(book['rank_last_week']),
                    'title': book['title'],
                    'author': book['author'],
                    'description': book['description'],
                    'amazon_link': book['amazon_product_url'],
                    'publisher': book['publisher']
                }
            top_list.append(books_dict)

    except ValueError:
        # Pass along a message that the API did not respond
        books_dict = {}
        books_dict['rank'] = 'The API is not responding'
        top_list.append(books_dict)
        # mail_admins('Books API', 'Looks like the Books API failed.')

    return nyt_list_date, top_list
