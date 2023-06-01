import pytest
@pytest.mark.login
def test1():
    a=3
    b=4
    assert a+1==b,"test failed"
    assert a==b,"failed"
@pytest.mark.login
def test2():
    name="selenium"
    assert name.upper()=='SELENIUM'
@pytest.mark.login
def test3():
    assert True
@pytest.mark.login
def test4():
    a=3
    b=2
    print(a+b)

