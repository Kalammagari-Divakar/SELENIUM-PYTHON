import pytest
@pytest.fixture()
def setup():
    print(" start ")
    yield
    print("end")

def test_method(setup):
    print('hello')
def test_method2(setup):
    print('world')