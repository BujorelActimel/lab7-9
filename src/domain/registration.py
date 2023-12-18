class Registration:
    id_counter = 0
    def __init__(self, guest_id, event_id, id_=None):
        if id_ is None:
            Registration.id_counter += 1
            self._id = Registration.id_counter
        else:
            Registration.id_counter = id_
            self._id = id_
        self._guest_id = guest_id
        self._event_id = event_id

    @property
    def id_(self):
        return self._id

    @property
    def guest_id(self):
        return self._guest_id

    @property
    def event_id(self):
        return self._event_id

    def __eq__(self, other):
        return self.id_ == other.id_

    def __str__(self):
        return f"""Registration(
    id={self._id}, 
    guest_id={self._guest_id}, 
    event_id={self._event_id}
)"""

    def __repr__(self):
        return str(self)
