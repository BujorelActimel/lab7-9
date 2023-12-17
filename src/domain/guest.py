class Guest:
    id_counter = 0
    def __init__(self, name, address, id_ = None):
        self._name = name
        self._address = address
        if id_ is None:
            Guest.id_counter += 1
            self._id = Guest.id_counter
        else:
            self._id = id_
            Guest.id_counter = id_

    def __str__(self):
        return f"""Guest(
    id: {self.id_},
    name: {self.name},
    address: {self.address}
)"""

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.id_ == other.id_

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address
    
    @property
    def id_(self):
        return self._id
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @address.setter
    def address(self, new_address):
        self._address = new_address
