Feature: Book CRUD operations
  As a user of the CRUD API
  I want to perform Create, Read, Update, and Delete operations on books
  So that I can manage the book resource

  Scenario: Create a new book (POST)
    Given I have a book with title "Clean Code" and author "Robert C. Martin" published in 2008
    When I send a request to create the book
    Then the book should be successfully created

  Scenario: Retrieve all books (GET All)
    When I send a request to retrieve all books
    Then I should receive a list of books

  Scenario: Retrieve a specific book by ID (GET By ID)
    Given I have a book with title "Clean Code" and author "Robert C. Martin" published in 2008
    When I send a request to retrieve the book by its ID "671ab3b13af7c503e8d5c695"
    Then The book with title "Clean Code" should be returned

  Scenario: Update an existing book (PUT)
    Given I have a book with title "Clean Code" and author "Robert C. Martin" published in 2008
    When I send a request to create the book
    And I update the book to have title "The Cleanear Coder" and author "Robert C." published in 2010
    Then The book should be successfully updated with new title "The Cleanear Coder"

  Scenario: Delete an existing book (DELETE)
    Given I have a book with title "Clean Code" and author "Robert C. Martin" published in 2008
    When I send a request to create the book
    And I send a request to delete the book by its ID
    Then the book should be successfully deleted

