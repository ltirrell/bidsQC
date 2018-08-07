from ..bidsQC import atoi

def test_atoi_int():
    result = atoi(42)
    assert type(result) == int

def test_atoi_text():
    result = atoi('this is text')
    assert type(result) == str
