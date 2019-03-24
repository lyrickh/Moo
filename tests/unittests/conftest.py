import pytest
import api.customer_db


@pytest.fixture(scope="function")
def setup_db(request):
    api.customer_db._FAKE_DB = list()

    def teardown():
        api.customer_db._FAKE_DB = list()

    request.addfinalizer(teardown)
