import random
import string
from event import Event
from guest import Guest
from datetime import date, time


def add_event(event_date: date, event_time: time, event_description: str, event_list: list):
    event_list.append(Event(event_date, event_time, event_description))


def add_guest(guest_name, guest_address, guest_list: list):
    guest_list.append(Guest(guest_name, guest_address))


def getGuestById(guest_list, guest_id: str):
        for guest in guest_list:
            if guest.getGuestId() == guest_id:
                return guest
        raise ValueError("Invitatul nu exista, incercati un id valid")


def getEventById(event_list, event_id: str):
    for event in event_list:
        if event.getEventId() == event_id:
            return event
    raise ValueError("Evenimentul nu exista, incercati un id valid")


def getGuestByName(guest_list: list, name: str):
    guests_found = []
    for guest in guest_list:
        if guest.getGuestName() == name:
            guests_found.append(guest)
    if len(guests_found) == 0:
        raise ValueError("Invitatul nu exista, incercati un nume valid")
    if len(guests_found) > 1:
        guests_found_ids = {guest.getGuestAddress():guest.getGuestId() for guest in guests_found}
        raise KeyError(f"Exista mai mult de un invitat cu numele '{guests_found[0].getGuestName()}', introduceti id-ul invitatului\n{guests_found_ids}\n>>>")
    return guests_found[0]


def getEventByDescrpition(event_list: list, description: str):
    for event in event_list:
        if event.getEventDescription() == description:
            return event
    raise ValueError("Evenimentul nu exista, incercati o descriere valida")


def delete_event(description, event_list):
    for index, event in enumerate(event_list):
        if event.getEventDescription() == description:
            event_list.pop(index)
            del event
            return
    raise ValueError("Evenimentul nu exista, incercati o descriere valida")


def delete_guest(name, guest_list):
    for index, guest in enumerate(guest_list):
        if guest.getGuestName() == name:
            guest_list.pop(index)
            del guest
            return
    raise ValueError("invitatul nu exista, incercati un nume valid")


def raport_guest_events(name, guest_list, event_list):
    guest = getGuestByName(guest_list, name)
    res = []
    for event_id in guest.getGuestEvents():
        res.append(getEventById(event_list, event_id))
    if len(res) == 0:
        raise ValueError(f"{guest.getGuestName()} nu este inscris la niciun eveniment")
    return sorted(res, key=Event.getEventDate)


def add_random_guest(guest_list):
    random_name = ""
    random_addres = "Strada "
    for i in range(random.randint(5, 8)):
        random_name += random.choice(string.ascii_lowercase)
    
    for i in range(random.randint(12, 15)):
        random_addres += random.choice(string.ascii_letters)

    random_guest = Guest(random_name, random_addres)
    guest_list.append(random_guest)


def add_random_event(event_list):
    random_year = random.randint(1, 2024)
    random_month = random.randint(1, 12)
    random_day = random.randint(1, 30)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)

    random_date = date(random_year, random_month, random_day)
    random_time = time(random_hour, random_minute)

    random_description = "'"
    for i in range(random.randint(12, 15)):
        random_description += random.choice(string.ascii_letters)
    random_description += "'"
    
    random_event = Event(random_date, random_time, random_description)
    event_list.append(random_event)


def modify_event(event_id, event_date, event_time, event_description, event_list):
    event = getEventById(event_list, event_id)

    event.setEventDate(event_date)
    event.setEventTime(event_time)
    event.setEventDescription(event_description)


def modify_guest(guest_id, guest_name, guest_address, guest_list):
    guest = getGuestById(guest_list, guest_id)

    guest.setGuestName(guest_name)
    guest.setGuestAddress(guest_address)