from src.math_operations import add,sub

def test_add():
    assert add(5,3)==8
    assert add(2,3)==5
    assert add(3,4)==7

def test_sub():
    assert sub(9,7)==2
    assert sub(5,4)==1
    assert sub(4,1)==3
    assert sub(10,5)==5    
