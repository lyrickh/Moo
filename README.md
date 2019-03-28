# Address Book API

API that provides the ability to search an address book for a customer based on surname

## Installation Instructions
Requires Docker to be installed

1. cd to the project directory (Moo)
2. run cmd "docker build -t python-moo ."
3. run cmd "docker run -d -p 5000:5000 python-moo"
4. The application is now running on http://127.0.0.1:5000/ !

## How to use the API
Navigate to "http://127.0.0.1:5000/search/surname"  to search for all customers with a given surname from the
csv of mock data.

Specific individual customers can be retrieved using the url "http://127.0.0.1:5000/search/surname/index" where
index is the location of the customer desired in the list of all customers with a given surname (i.e. 0 for the first
entry)

## Credit
Mock data generated from https://www.mockaroo.com