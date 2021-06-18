import pytest


def is_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True

@pytest.mark.parametrize('a', [-1, 0, 1, 4], ids = ['below zero', 'zero', 'one', 'valid'])
@pytest.mark.parametrize('b', [-1, 0, 1, 4], ids = ['below zero', 'zero', 'one', 'valid'])
@pytest.mark.parametrize('c', [-1, 0, 1, 4], ids = ['below zero', 'zero', 'one', 'valid'])
def test_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        assert is_triangle(a, b, c) == False
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        assert is_triangle(a, b, c) == False
    else:
        assert is_triangle(a, b, c) == True