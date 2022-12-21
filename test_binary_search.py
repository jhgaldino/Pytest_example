from binary_search import binary_search
import pytest

def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 4) == 3
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([], 1) == -1

if __name__ == '__main__':
    pytest.main()
