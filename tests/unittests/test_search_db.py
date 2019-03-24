import api.customer_db as db


def test_add_customer_data(setup_db):
    customer = dict(first_name='Lei', last_name='Ferretti')
    db.add_customer_to_db(customer)

    assert len(db.CUSTOMER_DATA) == 1
    assert db.CUSTOMER_DATA[0] == customer


def test_search_customers_by_field(setup_db):
    customer = dict(first_name='John', last_name='Doe')
    customer2 = dict(first_name='Alice', last_name='Doe')

    db.add_customer_to_db(customer)
    db.add_customer_to_db(customer2)

    results = db.search_customers_by_field("last_name", "Doe")

    assert results == [customer, customer2]

    results = db.search_customers_by_field("first_name", "Alice")

    assert results == [customer2]

    results = db.search_customers_by_field("last_name", "nonsense")

    assert  results == []

    results = db.search_customers_by_field("nonsense", "nonsense")

    assert results == []
