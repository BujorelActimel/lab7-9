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

    def unregister(self, guest, event):
        if guest.getGuestId() not in event.getEventGuests():
            raise ValueError(f"{guest.getGuestName()} nu este inscris la {event.getEventDescription()}")
        guest.unregisterFromEvent(event)
        event.unregisterGuest(guest)
        for index, log in enumerate(self.getLogs()):
            if log.getGuest().getGuestId() == guest.getGuestId() and log.getEvent().getEventId() == event.getEventId():
                self.getLogs().pop(index)
                del log
                return

    # Lista de evenimente la care participă o persoană, ordonată alfabetic după descriere sau după dată.
    def getEventsByGuest(self, guest):
        events = []
        for log in self.getLogs():
            if log.getGuest() == guest:
                events.append(log.getEvent())
        return events

    # Persoanele participante la cele mai multe evenimente.
    def getGuestsByMostEvents(self):
        guests = {}
        for log in self.getLogs():
            if log.getGuest().getGuestName() not in guests:
                guests[log.getGuest().getGuestName()] = 1
            else:
                guests[log.getGuest().getGuestName()] += 1 
        
        guests = {k: v for k, v in sorted(guests.items(), key=lambda item: item[1], reverse=True)}
        return guests

    # Evenimentele cu cei mai mulți participanți, afișând descrierea și numărul de participanți.
    def getEventsByMostGuests(self):
        events = {}
        for log in self.getLogs():
            if log.getEvent().getEventDescription() not in events:
                events[log.getEvent().getEventDescription()] = 1
            else:
                events[log.getEvent().getEventDescription()] += 1 
        
        events = {k: v for k, v in sorted(events.items(), key=lambda item: item[1], reverse=True)}
        return events
