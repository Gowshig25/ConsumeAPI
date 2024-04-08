

from src.consumeAPI.get_data import get_data_from_API
from src.consumeAPI.post_data import post_data


def test_getURL_method():
    valid=json_data()
    post_data(valid)
    assert valid in get_data_from_API()
def json_data():
    data={
        "p_id":100,
        "p_name":'nothing',
        "p_price":1234,
        "p_quantity":12
    }
    return data
'''
with pytest.raises(SystemExist):
    Inside block
where inside block must shown an SystemExit error otherwise thye test is fail
'''
