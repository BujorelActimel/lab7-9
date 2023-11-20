# from event import Event
# from guest import Guest
from datetime import datetime

class Log:
    def __init__(self, event, guest):
        self.event = event
        self.guest = guest
        self.logTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def getEvent(self):
        return self.event

    def getGuest(self):
        return self.guest

    def getTime(self):
        return self.logTime


class RegistrationLog:
    def __init__(self):
        self.logs = []

    def __str__(self):
        log_string = "Logs:\n"
        for log in self.getLogs():
            log_string += f"{log.getTime()}: {log.getGuest().getGuestName()} registered to {log.getEvent().getEventDescription()}\n"
        return log_string

    def getLogs(self):
        return self.logs

    def register(self, guest, event):
        guest.registerToEvent(event)
        event.registerGuest(guest)
        self.logs.append(Log(event, guest))
