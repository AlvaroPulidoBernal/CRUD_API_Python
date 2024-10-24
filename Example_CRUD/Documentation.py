

"""

In order to use the script with the test is neccessary to update the api key provided by the crud page
And change it in the test_CRUD_api.py file under Test -> Steps_definitions

No Issues where encounter during test.
The test are simple so is expected

BDD was used due to an easy way to understand test cases and can be read by anyone also provides a way to input custom data for testing

    Tests made using books as the base resource:
    Details of each book: Title, Autor and Year
        BOOK_DATA = {
                "title": book_name,
                "author": autor,
                "year": year)
        }

        POST: Add a book
        GET: Obtain all entries from the API
        GET: Obtain one entry using an ID as a parameter
        PUT: Modify an entry using an ID as a parameter
        DELETE: Remove an entry by its ID


    
Issues Encountered During Implementation
-   Limited amount of request, is not a blocker but limits the amount of test to run if is the first time using the API making you to stay simple and keep more complex cases as text and not as test 
        and the data is deleted after 24 hours
-   Since BDD is used the can lead to an issue in which the step was not found, easy way to fix this



Edge Cases Considered but Not Implemented
-   Handling Invalid Payloads which would be null values either all of the object, some fields Ex: Add the autor but not the year of the title different format in the JSON data
-   Concurrent request when trying to update at the same time a resourse
-   Length of the values allowed to enter 


Additional Insights and Recommendations
-   The API being able to provide more requests a day
-   Implement a way to clean up the test data after each test
-   Robust error handling
-   File management to use custom data from it and any configuration

"""