from guest import Guest
from event import Event
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

def test_registerToEvent():
    guest = Guest("Alin", "Strada Plopilor, nr.1")
    event = Event(date(2023, 11, 11), time(12, 30))

    guest.registerToEvent(event)
    assert guest.getGuestEvents() == {event.getEventId()}
    assert event.getEventGuests() == {guest.getGuestId()}

    # check for duplicate registration
    guest.registerToEvent(event)
    assert guest.getGuestEvents() == {event.getEventId()} 
    assert event.getEventGuests() == {guest.getGuestId()}


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
