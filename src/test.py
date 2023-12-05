import random
from business import *
from guest import Guest
from event import Event
from ui import *
from registrationLog import RegistrationLog
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

    test_description = "'GFzYtEwLnGisiW'"

    assert random_event.getEventDescription() == test_description


def test_extract_description():
    event_list = []
    add_event(date(2023, 12, 20), time(12, 30), "'Olimpiada de sah'", event_list)
    command = "cauta eveniment 'Olimpiada de sah'"
    command = command.split()
    assert extract_description(command) == "'Olimpiada de sah'"


def test_top_guests():
    guest1 = Guest("alin1", "str. Trotusului")
    guest2 = Guest("alin2", "str. Trotusului")
    guest3 = Guest("alin3", "str. Trotusului")
    guest4 = Guest("alin4", "str. Trotusului")
    guest5 = Guest("alin5", "str. Trotusului")
    guest_list = [guest1, guest2, guest3, guest4, guest5]

    event1 = Event(date(2023, 12, 10), time(12, 30), "'descriere1'")
    event2 = Event(date(2023, 12, 10), time(12, 30), "'descriere2'")
    event3 = Event(date(2023, 12, 10), time(12, 30), "'descriere3'")
    event4 = Event(date(2023, 12, 10), time(12, 30), "'descriere4'")
    event5 = Event(date(2023, 12, 10), time(12, 30), "'descriere5'")
    event_list = [event1, event2, event3, event4, event5]

    log = RegistrationLog()

    log.register(guest1, event1)
    log.register(guest1, event2) # guest1 = 2 events
    
    log.register(guest2, event1)
    log.register(guest2, event2)
    log.register(guest2, event5) # guest2 = 3 events
    
    log.register(guest3, event1) # guest3 = 1 events

                                 # guest4 = 0 events
                                 # guest5 = 0 events
    
    assert top_guests(guest_list) == [
        ["alin2", 3],
        ["alin1", 2],
        ["alin3", 1],
        ["alin4", 0],
        ["alin5", 0],
    ]

def test_top_events():
    guest1 = Guest("alin1", "str. Trotusului")
    guest2 = Guest("alin2", "str. Trotusului")
    guest3 = Guest("alin3", "str. Trotusului")
    guest4 = Guest("alin4", "str. Trotusului")
    guest5 = Guest("alin5", "str. Trotusului")
    guest_list = [guest1, guest2, guest3, guest4, guest5]

    event1 = Event(date(2023, 12, 10), time(12, 30), "'descriere1'")
    event2 = Event(date(2023, 12, 10), time(12, 30), "'descriere2'")
    event3 = Event(date(2023, 12, 10), time(12, 30), "'descriere3'")
    event4 = Event(date(2023, 12, 10), time(12, 30), "'descriere4'")
    event5 = Event(date(2023, 12, 10), time(12, 30), "'descriere5'")
    event_list = [event1, event2, event3, event4, event5]

    log = RegistrationLog()

    log.register(guest1, event1)
    log.register(guest2, event1) # event1 = 2 guests

    log.register(guest1, event2)
    log.register(guest2, event2)
    log.register(guest3, event2) # event2 = 3 guests

    log.register(guest1, event3) # event3 = 1 guests
                                 # event4 = 0 guests
                                 # event5 = 0 guests
    
    assert top_events(event_list) == [
        ["'descriere2'", 3],
        ["'descriere1'", 2],
        ["'descriere3'", 1],
        ["'descriere4'", 0],
        ["'descriere5'", 0],
    ]



# File tests
def test_save_events_to_csv():
    with open("data/test.csv", "w") as file:
        file.write("")

    event_list = []
    add_event(date(2023, 12, 20), time(12, 30), "'Olimpiada de sah'", event_list)

    save_events_to_csv("data/test.csv", event_list)

    with open("data/test.csv", "r") as file:
        lines = file.readlines()
        assert lines[1] == f"{event_list[0].getEventId()},2023-12-20,12:30:00,'Olimpiada de sah'\n"


def test_save_guests_to_csv():
    with open("data/test.csv", "w") as file:
        file.write("")

    guest_list = []
    add_guest("Alin", "Strada Plopilor, nr.1", guest_list)

    save_guests_to_csv("data/test.csv", guest_list)

    with open("data/test.csv", "r") as file:
        lines = file.readlines()
        assert lines[1] == f"{guest_list[0].getGuestId()},Alin,Strada Plopilor, nr.1\n"


def test_save_logs_to_csv():
    with open("data/test.csv", "w") as file:
        file.write("")

    guest_list = []
    add_guest("Alin", "Strada Plopilor, nr.1", guest_list)

    event_list = []
    add_event(date(2023, 12, 20), time(12, 30), "'Olimpiada de sah'", event_list)

    log = RegistrationLog()
    log.register(guest_list[0], event_list[0])

    save_logs_to_csv("data/test.csv", log)

    with open("data/test.csv", "r") as file:
        lines = file.readlines()
        assert lines[1] == f"{guest_list[0].getGuestId()},{event_list[0].getEventId()}\n"


def test_get_guests_from_csv():
    with open("data/test.csv", "w") as file:
        file.write("id,name,address\n1,Alin,Strada Plopilor nr.1\n")

    guest_list = get_guests_from_csv("data/test.csv")

    assert guest_list[0].getGuestId() == "1"
    assert guest_list[0].getGuestName() == "Alin"
    assert guest_list[0].getGuestAddress() == "Strada Plopilor nr.1"


def test_get_events_from_csv():
    with open ("data/test.csv", "w") as file:
        file.write("id,date,time,description\n1,2023-12-20,12:30:00,'Olimpiada de sah'\n")
    
    event_list = get_events_from_csv("data/test.csv")

    assert event_list[0].getEventId() == "1"
    assert event_list[0].getEventDate() == date(2023, 12, 20)
    assert event_list[0].getEventTime() == time(12, 30)
    assert event_list[0].getEventDescription() == "'Olimpiada de sah'"


def test_get_logs_from_csv():
    guest_list = []
    add_guest("Alin", "Strada Plopilor, nr.1", guest_list)

    event_list = []
    add_event(date(2023, 12, 20), time(12, 30), "'Olimpiada de sah'", event_list)

    with open("data/test.csv", "w") as file:
        file.write(f"guestId,eventId\n{guest_list[0].getGuestId()},{event_list[0].getEventId()}\n")

    logs = get_logs_from_csv("data/test.csv", guest_list, event_list)

    assert logs.getLogs()[0].getGuest().getGuestName() == "Alin"
    assert logs.getLogs()[0].getEvent().getEventDescription() == "'Olimpiada de sah'"
