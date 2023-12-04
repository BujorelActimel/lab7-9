# evenimente: <ID>, <dată>, <timp>, <descriere>
import uuid
import datetime

class Event:
    def __init__(self, date: datetime.date, time: datetime.time, description = "", eventId = None):
        if eventId:
            self.eventId = eventId
        else:
            self.eventId = str(uuid.uuid4())
        self.date = date
        self.time = time
        self.description = description
        self.guests = set() # set of guest id's

    def __str__(self):
        return f"{self.getEventDescription()}: {self.getEventDate()}, {self.getEventTime()}, id={self.getEventId()}"

    def __repr__(self):
        return str(self)
    
    def getEventId(self):
        return self.eventId
    
    def getEventDate(self):
        return self.date

    def getEventTime(self):
        return self.time

    def getEventDescription(self):
        return self.description

    def getEventGuests(self):
        return self.guests

    def getNumberOfGuests(self):
        return len(self.getEventGuests())

    def setEventDate(self, new_date: datetime.date):
        self.date = new_date

    def setEventTime(self, new_time: datetime.time):
        self.time = new_time

    def setEventDescription(self, new_description: str):
        self.description = new_description

    def registerGuest(self, guest: "Guest"):
        self.guests.add(guest.getGuestId())
