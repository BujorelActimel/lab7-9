import pytest
from domain import Registration

def test_registration_id_counter():
    Registration.id_counter = 0
    registration = Registration(1, 2)
    assert registration.id_ == 1
    registration = Registration(1, 2)
    assert registration.id_ == 2

def test_registration():
    registration = Registration(1, 2, id_=3)
    assert registration.guest_id == 1
    assert registration.event_id == 2
    assert registration.id_ == 3

def test_registration_str():
    registration = Registration(1, 2, id_=3)
    assert str(registration) == """Registration(
    id=3, 
    guest_id=1, 
    event_id=2
)"""