import pytest

def is_triangle(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True

@pytest.mark.parametrize('a', [-1, 0, 1, 4], ids = ['отрицательное', 'ноль', 'единица', 'валидное'])
@pytest.mark.parametrize('b', [-1, 0, 1, 4], ids = ['отрицательное', 'ноль', 'единица', 'валидное'])
@pytest.mark.parametrize('c', [-1, 0, 1, 4], ids = ['отрицательное', 'ноль', 'единица', 'валидное'])
def test_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        assert test_triangle(a, b, c) == False
    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        assert test_triangle(a, b, c) == False
    else:
        assert test_triangle(a, b, c) == True




