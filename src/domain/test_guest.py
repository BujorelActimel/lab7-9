import pytest
from domain import Guest

def setup_function():
    global guest1, guest2, guest3
    guest1 = Guest("John Doe", "123 Main St.", id_ = 1)
    guest2 = Guest("John Doe", "123 Main St.", id_ = 2)
    guest3 = Guest("Jane Doe", "123 Main St.", id_ = 3)

def test_init():
    assert guest1.id == 1
    assert guest1.name == "John Doe"
    assert guest1.address == "123 Main St."

def test_eq():
    with pytest.raises(AssertionError):
        assert guest1 == guest2
    assert guest1 != guest3

def test_getters():
    assert guest1.id == 1
    assert guest1.name == "John Doe"
    assert guest1.address == "123 Main St."

def test_setters():
    guest1.name = "Jane Doe"
    guest1.address = "456 Main St."
    assert guest1.name == "Jane Doe"
    assert guest1.address == "456 Main St."
