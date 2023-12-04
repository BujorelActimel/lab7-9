# from event import Event
# from guest import Guest
from datetime import datetime

class Log:
    def __init__(self, event, guest):
        self.event = event
        self.guest = guest
    
    def getEvent(self):
        return self.event

    def getGuest(self):
        return self.guest


class RegistrationLog:
    def __init__(self):
        self.logs = []

    def __str__(self):
        log_string = "Logs:\n"
        for log in self.getLogs():
            log_string += f"{log.getGuest().getGuestName()} s-a inscris la {log.getEvent().getEventDescription()}\n"
        return log_string

    def getLogs(self):
        return self.logs

    def register(self, guest, event):
        if guest.getGuestId() in event.getEventGuests():
            raise ValueError(f"{guest.getGuestName()} este deja inscris la {event.getEventDescription()}")
        guest.registerToEvent(event)
        event.registerGuest(guest)
        self.logs.append(Log(event, guest))

    # Lista de evenimente la care participă o persoană, ordonată alfabetic după descriere sau după dată.
    def getEventsByGuest(self, guest):
        events = []
        for log in self.getLogs():
            if log.getGuest() == guest:
                events.append(log.getEvent())
        return events

    # Persoanele participante la cele mai multe evenimente.
    def getGuestsByMostEvents(self):
        guests = []
        for log in self.getLogs():
            guests.append(log.getGuest())
        guests.sort(key=lambda x: len(self.getEventsByGuest(x)), reverse=True)
        return guests

    # Primele 20% evenimente cu cei mai mulți participanți, afișând descrierea și numărul de participanți.
    def getEventsByMostGuests(self):
        events = []
        for log in self.getLogs():
            events.append(log.getEvent())
        events.sort(key=lambda x: len(x.getGuests()), reverse=True)
        return events[:int(len(events)*0.2)]
