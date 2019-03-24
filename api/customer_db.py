"""
Pretend lightweight db, ideally this should be a sql database with indexes that can be queried, for speed
"""

from functools import lru_cache


CUSTOMER_DATA = list()


def add_customer_to_db(customer):
    """
    Add a customer
    :param customer: `dict` A dictionary representation of a customer
    :return:
    """
    global CUSTOMER_DATA
    CUSTOMER_DATA.append(customer)


@lru_cache
def search_customers_by_field(field, value):
    """
    Iterates through all customer data, returning rows where the column 'field' matches 'value'
    :param field: `str` column to search on
    :param value: `str` value to search for
    :return: `list` A list of dictionary representations of customers
    """
    results = []
    for customer in CUSTOMER_DATA:
        if customer.get(field) == value:
            results.append(customer)
    return results


def search_customers_by_surname(value):
    """
    Iterates through all customer data, returning rows where last_name is equal to 'value'
    :param value: `str` value to search for
    :return: `list` A list of dictionary representations of customers
    """
    return search_customers_by_field("last_name", value)
