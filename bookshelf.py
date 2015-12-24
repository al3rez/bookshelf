# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
import lxml.html


def get_authors_with_names_that_start_with(letter):
    URL = 'https://en.wikipedia.org/wiki/List_of_authors_by_name:_'
    response = requests.get(URL+letter.upper())
    element_tree = lxml.html.fromstring(response.text)
    authors = element_tree.xpath('//*[@id="mw-content-text"]/ul/li/a')
    return [author.text for author in authors]


def search_for_books_by_author(name):
    URL = 'https://www.goodreads.com/search'
    payload = {
        'utf8': '✓',
        'search[query]': name,
        'commit': 'Search',
        'search_type': 'books',
        'search[field]': 'on'
    }
    response = requests.get(URL, params=payload)
    element_tree = lxml.html.fromstring(response.text)
    books = element_tree.xpath('//*/a[@class="bookTitle"]')
    return [book.attrib['href'] for book in books]
