# test_CRUD_api.py
from pytest_bdd import scenarios, given, when, then, parsers
import requests

scenarios('CRUD_rest_api.feature')

api_id = "226e51010e744fb5ba3363e57f5be301"
BASE_URL = f'https://crudcrud.com/api/{api_id}/books'
BOOK_ID = None 

BOOK_DATA = {}
BOOK_LIST = []
BOOK_BY_ID = {}


@given(parsers.cfparse('I have a book with title {book_name} and author {autor} published in {year}'))
def book_payload(book_name, autor, year):
    global BOOK_DATA
    BOOK_DATA = {
        "title": book_name.strip('"'),
        "author": autor.strip('"'),
        "year": int(year.strip('"'))
    }
@when('I send a request to create the book')
def create_book():
    global BOOK_ID
    response = requests.post(BASE_URL, json=BOOK_DATA)
    assert response.status_code == 201  # Created
    BOOK_ID = response.json()['_id']



@then('the book should be successfully created')
def verify_book_creation():
    assert BOOK_ID is not None



@when('I send a request to retrieve all books')
def get_all_books():
    response = requests.get(BASE_URL)
    assert response.status_code == 200  # OK
    global BOOK_LIST
    BOOK_LIST = response.json()
@then('I should receive a list of books')
def verify_all_books_retrieved():
    assert isinstance(BOOK_LIST, list)



@when(parsers.cfparse('I send a request to retrieve the book by its ID {id}'))
def get_book_by_id(id : str):
    book_ID = id.strip('"')
    response = requests.get(f"{BASE_URL}/{book_ID}")
    assert response.status_code == 200  # OK
    global BOOK_BY_ID
    BOOK_BY_ID = response.json()
@then(parsers.cfparse('The book with title {title} should be returned'))
def verify_book_retrieved(title : str):
    assert BOOK_BY_ID['title'] == title.strip('"')



@when(parsers.cfparse('I update the book to have title {new_title} and author {new_autor} published in {new_year}'))
def update_book(new_title, new_autor, new_year):
    global BOOK_ID
    updated_data = {
        "title": new_title.strip('"'),
        "author": new_autor.strip('"'),
        "year": int(new_year.strip('"'))
    }
    response = requests.put(f"{BASE_URL}/{BOOK_ID}", json=updated_data)
    assert response.status_code == 200  # OK
@then(parsers.cfparse('The book should be successfully updated with new title {new_title}'))
def verify_book_updated(new_title):
    global BOOK_ID
    response = requests.get(f"{BASE_URL}/{BOOK_ID}")
    updated_book = response.json()
    assert updated_book['title'] == new_title.strip('"')



@when('I send a request to delete the book by its ID')
def delete_book():
    global BOOK_ID
    response = requests.delete(f"{BASE_URL}/{BOOK_ID}")
    assert response.status_code == 200  # OK
@then('the book should be successfully deleted')
def verify_book_deleted():
    global BOOK_ID
    response = requests.get(f"{BASE_URL}/{BOOK_ID}")
    assert response.status_code == 404  # Not Found