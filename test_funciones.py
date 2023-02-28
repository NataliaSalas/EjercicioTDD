from funciones import menor
def test_menor():
    assert menor([2,3,5,1,0,8])==0
    assert menor([2,3,5,1,9,8])==1
    assert menor([2,3,5,17,23,8])==2