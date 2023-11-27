# persoane: <personID>, <nume>, <adresă>
import uuid

class Guest:
    def __init__(self, name: str, address: str):
        self.guestId = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.events = set() # set of event id's

    def __str__(self):
        return f"{self.getGuestName()}: {self.getGuestAddress()}, id={self.getGuestId()}"

    def __repr__(self):
        return str(self)

    def getGuestId(self):
        return self.guestId
    
    def getGuestName(self):
        return self.name

    def getGuestAddress(self):
        return self.address

    def getGuestEvents(self):
        return self.events

    def getNumberOfEvents(self):
        return len(self.getGuestEvents())

    def setGuestName(self, new_name: str):
        self.name = new_name

    def setGuestAddress(self, new_address: str):
        self.address = new_address

    def registerToEvent(self, event: "Event"):
        self.events.add(event.getEventId())
