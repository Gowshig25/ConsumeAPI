import unittest

from src.consumeAPI.get_data import get_data_from_API
from src.consumeAPI.post_data import post_data


class test_unittest(unittest.TestCase):
    def test_add_product(self):
        data=postProduct()
        post_data(data)
        assert data in get_data_from_API()
def postProduct():
    data={
        'p_id':10,
        'p_name':'hockey Stick',
        'p_price':123.67,
        'p_quantity':100
    }
    return data
