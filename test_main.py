from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(10), BinaryNumber(2)) == 10*2
    assert quadratic_multiply(BinaryNumber(5),BinaryNumber(2)) == 5*2
    assert quadratic_multiply(BinaryNumber(20),BinaryNumber(1)) == 20
