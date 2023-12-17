class Event:
    id_counter = 0
    def __init__(self, date, time, description, id_ = None):
        self._date = date
        self._time = time
        self._description = description
        if id_ is None:
            Event.id_counter += 1
            self._id = Event.id_counter
        else:
            Event.id_counter = id_
            self._id = id_

    def __str__(self):
        return f"""Event(
    id: {self.id_}, 
    date: {self.date}, 
    time: {self.time},
    description: {self.description}
)"""

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.id_ == other.id_
    
    @property
    def date(self):
        return self._date
    
    @property
    def time(self):
        return self._time

    @property
    def description(self):
        return self._description

    @property
    def id_(self):
        return self._id
    
    @date.setter
    def date(self, new_date):
        self._date = new_date

    @time.setter
    def time(self, new_time):
        self._time = new_time

    @description.setter
    def description(self, new_description):
        self._description = new_description
