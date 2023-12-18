from domain import Event, Guest, Registration

class Service:
    def __init__(self, repository):
        self._repository = repository

    @property
    def repo(self):
        return self._repository

    def add_event(self, event_date, event_time, event_description):
        self.repo.events.append(Event(event_date, event_time, event_description))

    def update_event(self, event_id, event_date, event_time, event_description):
        event = self.repo.find_event(event_id)
        if not event_date:
            pass
        else:
            event.date = event_date
        if not event_time:
            pass
        else:
            event.time = event_time
        if not event_description:
            pass
        else:
            event.description = event_description

    def delete_event(self, event_id):
        event_to_delete = self.repo.find_event(event_id)
        self.repo.events.remove(event_to_delete)
        Event.id_counter -= 1

    def add_guest(self, guest_name, guest_address):
        self.repo.guests.append(Guest(guest_name, guest_address))

    def update_guest(self, guest_id, guest_name, guest_address):
        guest = self.repo.find_guest(guest_id)
        if not guest_name:
            pass
        else:
            guest.name = guest_name
        if not guest_address:
            pass
        else:
            guest.address = guest_address

    def delete_guest(self, guest_id):
        guest = self.repo.find_guest(guest_id)
        self.repo.guests.remove(guest)
        Guest.id_counter -= 1

    def register(self, guest_id, event_id):
        try:
            self.repo.find_guest(guest_id)
        except ValueError:
            raise ValueError("Guest not found.")
        try:
            self.repo.find_event(event_id)
        except ValueError:
            raise ValueError("Event not found.")

        for registration in self.repo.registrations:
            if registration.guest_id == guest_id and registration.event_id == event_id:
                raise ValueError("Guest already registered to event.")

        self.repo.registrations.append(Registration(guest_id, event_id))

    def sort_guest_events_by_description_and_date(self, guest_id):
        guest_events = []
        for registration in self.repo.registrations:
            if registration.guest_id == guest_id:
                guest_events.append(self.repo.find_event(registration.event_id))
        guest_events.sort(key=lambda event: (event.description, event.date))
        return guest_events

    def guest_number_of_registrations(self, guest_id):
        num_of_registrations = 0
        for registration in self.repo.registrations:
            if registration.guest_id == guest_id:
                num_of_registrations += 1
        return num_of_registrations

    def sort_guests_by_registrations(self):
        guests = []
        for guest in self.repo.guests:
            guests.append(guest)
        guests.sort(key=lambda guest: self.guest_number_of_registrations(guest.id_), reverse=True)
        return {guest.name: self.guest_number_of_registrations(guest.id_) for guest in guests}

    def event_number_of_registrations(self, event_id):
        num_of_registrations = 0
        for registration in self.repo.registrations:
            if registration.event_id == event_id:
                num_of_registrations += 1
        return num_of_registrations

    def sort_events_by_registrations(self):
        events = []
        for event in self.repo.events:
            events.append(event)
        events.sort(key=lambda event: self.event_number_of_registrations(event.id_), reverse=True)
        events = events[:len(events)//5]
        return {event.description: self.event_number_of_registrations(event.id_) for event in events}
