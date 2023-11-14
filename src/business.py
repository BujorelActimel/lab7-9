from event import Event
from guest import Guest
from datetime import date, time


def add_event(event_date: date, event_time: time, event_description: str, event_list: list):
    event_list.append(Event(event_date, event_time, event_description))


def add_guest(guest_name, guest_address, guest_list: list):
    guest_list.append(Guest(guest_name, guest_address))
