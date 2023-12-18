import os
from service import Service
from controller import Controller

class AppUI:

    def __init__(self, repository):
        self._repository = repository
        self._service = Service(self.repository)
        self._controller = Controller(self.service)

    @property
    def repository(self):
        return self._repository

    @property
    def service(self):
        return self._service
    
    @property
    def controller(self):
        return self._controller

    def mainloop(self):
        while True:
            os.system("cls")
            self.menu()
            selection = self.get_menu_selection()

            match selection:
                case 1:
                    self.controller.add_event()
                case 2:
                    self.controller.update_event()
                case 3:
                    self.controller.delete_event()
                case 4:
                    self.controller.add_guest()
                case 5:
                    self.controller.update_guest()
                case 6:
                    self.controller.delete_guest()
                case 7:
                    self.controller.view_events()
                case 8:
                    self.controller.view_guests()
                case 9:
                    self.controller.search_event()
                case 10:
                    self.controller.search_guest()
                case 11:
                    self.controller.register()
                case 12:
                    self.controller.view_registrations()
                case 0:
                    self.controller.exit()
                    return

    def menu(self):
        print("""Menu:
    1. Add event
    2. Update event
    3. Delete event
    4. Add guest
    5. Update guest
    6. Delete guest
    7. View events
    8. View guests
    9. Search event
    10. Search guest
    11. Register
    12. View registrations
    0. Exit
    """)

    def get_menu_selection(self):
        valid_selections = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        while True:
            try:
                selection = int(input("Enter selection: "))
                if selection not in valid_selections:
                    raise ValueError
                return selection
            except ValueError:
                print("Invalid input. Please try again.")
