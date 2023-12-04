import copy
import random
import string
from event import Event
from guest import Guest
from datetime import date, time
from registrationLog import RegistrationLog


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


def search_event(event_description, event_list):
    event = getEventByDescrpition(event_list, event_description)
    return f"id={event.getEventId()}\ndescriere={event.getEventDescription()}\ndata={event.getEventDate()}\ntimp={event.getEventTime()}"


def search_guest(guest_name, guest_list):
    guest = getGuestByName(guest_list, guest_name)
    return f"id={guest.getGuestId()}\nnume={guest.getGuestName()}\nadresa={guest.getGuestAddress()}"


def top_guests(guest_list):
    sorted_guests = sorted(guest_list, key=lambda x: x.getNumberOfEvents(), reverse=True)
    
    leaderboard = [[guest.getGuestName(), guest.getNumberOfEvents()] for guest in sorted_guests]

    return leaderboard


def top_events(event_list):
    sorted_events = sorted(event_list, key=lambda x: x.getNumberOfGuests(), reverse=True)

    leaderboard = [[event.getEventDescription(), event.getNumberOfGuests()] for index, event in enumerate(sorted_events)]
    # leaderboard = leaderboard[:(len(leaderboard) // 5 - 1)]

    return leaderboard


def save_events_to_csv(file, event_list):
    with open(file, "w") as f:
        f.write("id,Date,Time,Description\n")
        for event in event_list:
            f.write(f"{event.getEventId()},{event.getEventDate()},{event.getEventTime()},{event.getEventDescription()}\n")


def save_guests_to_csv(file, guest_list):
    with open(file, "w") as f:
        f.write("id,Name,Address\n")
        for guest in guest_list:
            f.write(f"{guest.getGuestId()},{guest.getGuestName()},{guest.getGuestAddress()}\n")


def save_logs_to_csv(file, registration_log):
    with open(file, "w") as f:
        f.write("GuestId,EventId\n")
        for log in registration_log.getLogs():
            f.write(f"{log.getGuest().getGuestId()},{log.getEvent().getEventId()}\n")


def get_events_from_csv(file):
    event_list = []
    with open(file, "r") as f:
        for line in f.readlines()[1:]:
            event = line.split(",")
            event_year, event_month, event_day = list(map(int, event[1].split("-")))
            try:
                event_hour, event_minute = list(map(int, event[2].split(":")))
            except ValueError:
                event_hour, event_minute, event_second = list(map(int, event[2].split(":")))
            event_list.append(Event(date(event_year, event_month, event_day), time(event_hour, event_minute), event[3].strip(), event[0]))
    return event_list


def get_guests_from_csv(file):
    guest_list = []
    with open(file, "r") as f:
        for line in f.readlines()[1:]:
            guest = line.split(",")
            guest_list.append(Guest(guest[1], guest[2].strip(), guest[0]))
    return guest_list


def get_logs_from_csv(file, guest_list, event_list):
    registration_log = RegistrationLog()
    with open(file, "r") as f:
        for line in f.readlines()[1:]:
            log = line.split(",")
            registration_log.register(getGuestById(guest_list, log[0]), getEventById(event_list, log[1].strip()))
    return registration_log
