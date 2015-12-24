from bookshelf import (get_authors_with_names_that_start_with,
                      search_for_books_by_author,
                      create_html_element_from)

from lxml.html import HtmlElement
import requests


def test_that_it_gets_a_list_of_authors():
    authors = get_authors_with_names_that_start_with('M')
    assert isinstance(authors, list)


def test_that_it_gets_a_list_of_books():
    books = search_for_books_by_author('Damian Marrett')
    assert isinstance(books, list)

def test_that_it_creates_html_element_from_response():
    URL = 'https://en.wikipedia.org/wiki/List_of_authors_by_name:_M'
    response = requests.get(URL)
    assert isinstance(create_html_element_from(response), HtmlElement)

