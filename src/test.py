import random
from business import *
from guest import Guest
from event import Event
from ui import *
from datetime import date, time

# Test the 'Guest' class: 
def test_getGuestName():
    guest = Guest("Alin", "...")
    assert guest.getGuestName() == "Alin" 

def test_getGuestAdress():
    guest = Guest("...", "Strada Plopilor, nr.1")
    assert guest.getGuestAddress() == "Strada Plopilor, nr.1"

def test_setGuestName():
    guest = Guest("...", "Strada Plopilor, nr.1")
    guest.setGuestName("Alin")
    assert guest.getGuestName() == "Alin"

def test_setGuestAddress():
    guest = Guest("Alin", "...")
    guest.setGuestAddress("Strada Plopilor, nr.1")
    assert guest.getGuestAddress() == "Strada Plopilor, nr.1"


# Test the 'Event' class:
def test_getEventDate():
    event = Event(date(2023, 11, 11), time(12, 30))
    assert event.getEventDate() == date(2023, 11, 11)

def test_getEventTime():
    event = Event(date(2023, 11, 11), time(12, 30))
    assert event.getEventTime() == time(12, 30)

def test_getEventDescription():
    event = Event(date(2023, 11, 11), time(12, 30), "test passed")
    assert event.getEventDescription() == "test passed"

def test_getEventGuests():
    guest1 = Guest("...", "...")
    guest2 = Guest("...", "...")
    event = Event(date(2023, 11, 11), time(12, 30))
    event.guests = {guest1.getGuestId(), guest2.getGuestId()}
    assert event.getEventGuests() == {guest1.guestId, guest2.guestId}

def test_setEventDate():
    event = Event(date(2023, 11, 11), time(12, 30))
    event.setEventDate(date(2023, 12, 12))
    assert event.getEventDate() == date(2023, 12, 12)

def test_setEventTime():
    event = Event(date(2023, 11, 11), time(12, 30))
    event.setEventTime(time(13, 45))
    assert event.getEventTime() == time(13, 45)

def test_setEventDescription():
    event = Event(date(2023, 11, 11), time(12, 30), "test failed")
    event.setEventDescription("test passed")
    assert event.getEventDescription() == "test passed"

def test_registerGuest():
    event = Event(date(2023, 11, 11), time(12, 30))
    guest = Guest("...", "...")

    event.registerGuest(guest)
    assert event.getEventGuests() == {guest.getGuestId()}

    # check for duplicate registration
    event.registerGuest(guest)
    assert event.getEventGuests() == {guest.getGuestId()}


# Test the ui:
def test_valid_date():
    assert valid_date("2023-10-19")
    assert not valid_date("2023 10 19")
    assert not valid_date("2023-10 19")
    assert not valid_date("2023-10")
    assert not valid_date("19-10-2023")
    assert not valid_date("")

def test_valid_time():
    assert valid_time("12:30")
    assert valid_time("00:00")
    assert not valid_time("30:12")
    assert not valid_time("12")
    assert not valid_time("25:13")
    assert not valid_time("24:00")
    assert not valid_time("")

def test_valid_description():
    assert valid_description("'descriere'")
    assert valid_description("'''''")
    assert valid_description("'''")
    assert valid_description("''")
    assert not valid_description("'descriere")
    assert not valid_description("descriere'")
    assert not valid_description("descriere")
    assert not valid_description("")


def test_add_random_guest():
    random.seed(0)
    guest_list = []
    add_random_guest(guest_list)
    random_guest = guest_list[0]

    test_name = "ynbiqpmz"

    assert random_guest.getGuestName() == test_name


def test_add_random_event():
    random.seed(0)
    event_list = []
    add_random_event(event_list)
    random_event = event_list[0]

    test_description = "GFzYtEwLnGisiW"

    assert random_event.getEventDescription() == test_description
