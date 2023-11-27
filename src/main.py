# Done:  - add
#        - delete
#        - register
#        - raport: - invitat
#        - exit
#        - modify: - event
# 
# TODO : - modify: - invitat
#        - search
#        - unregister
#        - raport: - leaderboard
#                  - top events
#        - help

from ui import *
from business import *
from registrationLog import RegistrationLog

def main():
    registrations = RegistrationLog()
    all_guests, all_events = [], []

    while True:
        print_menu()
        command = get_command()
        try:
            validate_command(command)
        except (ValueError, IndexError) as error:
            enter(f"Eroare: {error}")
        else:        
            try:
                match command[0]:
                    case "adauga":
                        if command[1] == "eveniment":
                            add_event(extract_date(command), extract_time(command), extract_description(command), all_events)
                        
                        elif command[1] == "invitat":
                            add_guest(extract_name(command), extract_address(command), all_guests)
                        
                        elif command[1] == "random":
                            if command[2] == "invitat":
                                add_random_guest(all_guests)
                            elif command[2] == "eveniment":
                                add_random_event(all_events)

                    
                    case "sterge":
                        if command[1] == "eveniment":
                            try:
                                delete_event(extract_description(command), all_events)
                                enter("Evenimentul a fost sters cu succes")
                            except ValueError as error:
                                enter(f"Eroare: {error}")

                        elif command[1] == "invitat":
                            try:
                                delete_guest(extract_name(command), all_guests)
                                enter("Invitatul a fost sters cu succes")
                            except ValueError as error:
                                enter(f"Eroare: {error}")

                    case "modifica":
                        if command[1] == "eveniment":
                            command = " ".join(command)
                            command = command.split(maxsplit=5)
                            modify_event(extract_id(command), extract_date(command), extract_time(command), extract_description(command), all_events)
                        
                        if command[1] == "invitat":
                            modify_guest(extract_id(command), extract_name(command), extract_address(command), all_guests)

                    case "cauta":
                        pass


                    case "inscrie":
                        command[2] = " ".join(command[2:])
                        try:
                            guest = getGuestByName(all_guests, command[1])
                        except ValueError as error:
                            enter(f"Eroare: {error}")
                            continue
                        except KeyError as error:
                            try:
                                guest = getGuestById(all_guests, input(f"{error}"))
                            except ValueError as error:
                                enter(f"Eroare: {error}")
                                continue

                        try:
                            event = getEventByDescrpition(all_events, command[2])
                        except ValueError as error:
                            enter(f"Eroare: {error}")
                            continue

                        except KeyError as error:
                            try:
                                guest = getEventById(all_events, input(f"{error}"))
                            except ValueError as error:
                                enter(f"Eroare: {error}")
                                continue

                        else:
                            registrations.register(guest, event)
                            enter("Inregistrarea a fost facuta cu succes")


                    case "raport":
                        if command[1] == "invitat":
                            try:
                                enter(raport_guest_events(extract_name(command), all_guests, all_events))
                            except ValueError as error:
                                enter(error)
                

                    case "exit":
                        exit()


                    case "debug":
                        print(registrations)
                        enter(f"Guests: {all_guests}\nEvents: {all_events}")

            except IndexError:
                pass

if __name__ == "__main__":
    main()
