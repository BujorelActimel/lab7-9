# comenzi:
#     - adauga, sterge, modifica, cauta:
#         eveniment
#         invitat
#     - inscrie invitat la un eveniment
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

                    case "exit":
                        exit()

                    case "debug":
                        print(registrations)
                        enter(f"Guests: {all_guests}\nEvents: {all_events}")

            except IndexError:
                pass

if __name__ == "__main__":
    main()
