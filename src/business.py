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
