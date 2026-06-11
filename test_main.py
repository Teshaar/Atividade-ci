import pytest
from main import is_prime, calculate_factorial

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(17) == True
    assert is_prime(1) == False

def test_calculate_factorial():
    assert calculate_factorial(0) == 1
    assert calculate_factorial(5) == 120
    assert calculate_factorial(3) == 6
    
    with pytest.raises(ValueError):
        calculate_factorial(-1)