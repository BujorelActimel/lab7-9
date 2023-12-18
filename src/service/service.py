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
