from domain import Event, Guest, Registration
from datetime import date, time

class Repo:
    def __init__(self, events_file_name, guests_file_name, registrations_file_name):
        self._events_file_name = events_file_name
        self._guests_file_name = guests_file_name
        self._registrations_file_name = registrations_file_name
        self._events = self.load_events()
        self._guests = self.load_guests()
        self._registrations = self.load_registrations()

    @property
    def events(self):
        return self._events
    
    @property
    def guests(self):
        return self._guests

    @property
    def registrations(self):
        return self._registrations

    @property
    def events_file_name(self):
        return self._events_file_name

    @property
    def guests_file_name(self):
        return self._guests_file_name

    @property
    def registrations_file_name(self):
        return self._registrations_file_name

    def load_events(self):
        events = []
        with open(self.events_file_name, "r") as f:
            events_lines = f.readlines()
            for event_line in events_lines[1:]:
                event_line = event_line.strip()
                if event_line == "":
                    continue
                event_id, event_date, event_time, event_description = event_line.split(",")
                event_id = int(event_id)
                event_date = date.fromisoformat(event_date)
                event_time = time.fromisoformat(event_time)
                event = Event(event_date, event_time, event_description, id_=event_id)
                events.append(event)
        return events
    
    def load_guests(self):
        guests = []
        with open(self.guests_file_name, "r") as f:
            guests_lines = f.readlines()
            for guest_line in guests_lines[1:]:
                guest_line = guest_line.strip()
                if guest_line == "":
                    continue
                guest_id, guest_name, guest_address = guest_line.split(",")
                guest_id = int(guest_id)
                guest = Guest(guest_name, guest_address, id_=guest_id)
                guests.append(guest)
        return guests

    def load_registrations(self):
        registrations = []
        with open(self.registrations_file_name, "r") as f:
            registrations_lines = f.readlines()
            for registration_line in registrations_lines[1:]:
                registration_line = registration_line.strip()
                if registration_line == "":
                    continue
                registration_id, guest_id, event_id = registration_line.split(",")
                registration_id = int(registration_id)
                guest_id = int(guest_id)
                event_id = int(event_id)
                registration = Registration(guest_id, event_id, id_=registration_id)
                registrations.append(registration)
        return registrations

    def save_data(self):
        self.save_events()
        self.save_guests()
        self.save_registrations()

    def save_events(self):
        with open(self.events_file_name, "w") as f:
            f.write("id,date,time,description\n")
            for event in self.events:
                event_line = f"{event.id_},{event.date},{event.time},{event.description}\n"
                f.write(event_line)

    def save_guests(self):
        with open(self.guests_file_name, "w") as f:
            f.write("id,name,address\n")
            for guest in self.guests:
                guest_line = f"{guest.id_},{guest.name},{guest.address}\n"
                f.write(guest_line)
    
    def save_registrations(self):
        with open(self.registrations_file_name, "w") as f:
            f.write("id,guest_id,event_id\n")
            for registration in self.registrations:
                registration_line = f"{registration.id_},{registration.guest_id},{registration.event_id}\n"
                f.write(registration_line)

    def find_event(self, event_id):
        for event in self.events:
            if event.id_ == event_id:
                return event
        raise ValueError("Event ID not found.")

    def find_guest(self, guest_id):
        for guest in self.guests:
            if guest.id_ == guest_id:
                return guest
        raise ValueError("Guest ID not found.")

    def find_registration(self, registration_id):
        for registration in self.registrations:
            if registration.id_ == registration_id:
                return registration
        raise ValueError("Registration ID not found.")
