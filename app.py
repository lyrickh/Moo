#!/usr/bin/env python3

import json

from api.customer_db import search_customers_by_surname, add_customer_to_db
from api.read_csv_data import read_data_from_csv
from flask import Flask
app = Flask(__name__)


def initialise_db():
    customer_data = read_data_from_csv('./examples/MOCK_DATA.csv')
    for customer in customer_data:
        add_customer_to_db(customer)


@app.route('/')
def landing():
    return 'Search for customers using url "/search/<surname>", choose a specific customer with ' \
           '"/search/<surname>/<index>"'


@app.route('/search/<string:surname>', methods=['GET', 'POST'], defaults={'index': None})
@app.route('/search/<string:surname>/<int:index>', methods=['GET', 'POST'])
def search(surname, index):
    """ Return json list of dicts for all customers matching a given surname or single dict
        if index param is specified """
    customers = search_customers_by_surname(surname)

    if index is None:
        # Return list of dicts of all customers matching
        return json.dumps(customers)

    if len(customers) < index:
        return "Customer not found!"

    # Return single customer dict corresponding to index in the original returned list
    return json.dumps(customers[index])


if __name__ == '__main__':
    initialise_db()
    app.run(debug=True, host='0.0.0.0')
