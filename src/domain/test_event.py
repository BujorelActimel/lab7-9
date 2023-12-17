import pytest
from domain import Event

def setup_function():
    global event1, event2, event3
    event1 = Event("2022-12-31", "23:59", "New Year's Eve", id_ = 1)
    event2 = Event("2022-12-31", "23:59", "New Year's Eve", id_ = 2)
    event3 = Event("2022-12-24", "18:00", "Christmas Eve", id_ = 3)

def test_init():
    assert event1.id_ == 1
    assert event1.date == "2022-12-31"
    assert event1.time == "23:59"
    assert event1.description == "New Year's Eve"

def test_eq():
    with pytest.raises(AssertionError):
        assert event1 == event2
    assert event1 != event3

def test_getters():
    assert event1.id_ == 1
    assert event1.date == "2022-12-31"
    assert event1.time == "23:59"
    assert event1.description == "New Year's Eve"

def test_setters():
    event1.date = "2022-12-25"
    event1.time = "00:00"
    event1.description = "Christmas Day"
    assert event1.date == "2022-12-25"
    assert event1.time == "00:00"
    assert event1.description == "Christmas Day"
