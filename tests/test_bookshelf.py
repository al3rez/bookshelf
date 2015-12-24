from bookshelf import (search_for_books_by_author,
                      get_authors_with_names_that_start_with)


def test_that_it_gets_a_list_of_authors():
    authors = get_authors_with_names_that_start_with('M')
    assert isinstance(authors, list)


def test_that_it_gets_a_list_of_books():
    books = search_for_books_by_author('Damian Marrett')
    assert isinstance(books, list)
