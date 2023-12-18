import os
import utils

class Controller:
    def __init__(self, service):
        self._service = service

    @property
    def service(self):
        return self._service

    def add_event(self):
        event_date = utils.date_input()
        event_time = utils.time_input()
        event_description = utils.description_input()
        self.service.add_event(event_date, event_time, event_description)
        utils.enter("Event added.")

    def update_event(self):
        event_id = utils.id_input()
        event_date = utils.date_input()
        event_time = utils.time_input()
        event_description = utils.description_input()
        try:
            self.service.update_event(event_id, event_date, event_time, event_description)
        except AttributeError:
            utils.enter("Event not found.")
        else:
            utils.enter("Event updated.")

    def delete_event(self):
        event_id = utils.id_input()
        try:
            self.service.delete_event(event_id)
        except AttributeError:
            utils.enter("Event not found.")
        else:
            utils.enter("Event deleted.")

    def add_guest(self):
        guest_name = utils.name_input()
        guest_address = utils.address_input()
        self.service.add_guest(guest_name, guest_address)
        utils.enter("Guest added.")
    
    def update_guest(self):
        guest_id = utils.id_input()
        guest_name = utils.name_input()
        guest_address = utils.address_input()
        try:
            self.service.update_guest(guest_id, guest_name, guest_address)
        except AttributeError:
            utils.enter("Guest not found.")
        else:
            utils.enter("Guest updated.")

    def delete_guest(self):
        guest_id = utils.id_input()
        try:
            self.service.delete_guest(guest_id)
        except AttributeError:
            utils.enter("Guest not found.")
        else:
            utils.enter("Guest deleted.")
    
    def view_events(self):
        events = self.service.repo.events
        if not events:
            utils.enter("No events.")
            return
        for event in events:
            print(event)
        utils.enter()

    def view_guests(self):
        guests = self.service.repo.guests
        if not guests:
            utils.enter("No guests.")
            return
        for guest in guests:
            print(guest)
        utils.enter()
    
    def exit(self):
        os.system("cls")
        self.service.repo.save_data()
        print("Goodbye!")