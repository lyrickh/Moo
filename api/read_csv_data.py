def read_data_from_csv(file_name):
    """
    Loads in a csv file of customer address data and returns the customer info as a list of dicts

    :param file_name: `string` csv file to be read
    :return: `dict`
    """

    with open(file_name, encoding='utf8') as f:
        content = f.read()

    content = content.split("\n")
    headings, *customers = content
    headings = headings.split(',')

    customer_dicts = []
    for customer in customers:
        if customer:
            customer_dicts.append({k: v for k, v in zip(headings, customer.split(','))})

    return customer_dicts


if __name__ == "__main__":
    read_data_from_csv("../examples/MOCK_DATA.csv")