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
def hello_world():
    return 'Flask Dockerized'


@app.route('/search/<string:surname>', methods=['GET', 'POST'])
def search(surname):
    customers = search_customers_by_surname(surname)
    return json.dumps(customers)


if __name__ == '__main__':
    initialise_db()
    app.run(debug=True, host='0.0.0.0')
