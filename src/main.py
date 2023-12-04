from ui import *
from business import *
from registrationLog import RegistrationLog

def main():
    all_guests, all_events = get_guests_from_csv("data/guests.csv"), get_events_from_csv("data/events.csv")
    registrations = get_logs_from_csv("data/logs.csv", all_guests, all_events)

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
                                delete_event(extract_description(command), all_events, registrations)
                                enter("Evenimentul a fost sters cu succes")
                            except ValueError as error:
                                enter(f"Eroare: {error}")

                        elif command[1] == "invitat":
                            try:
                                delete_guest(extract_name(command), all_guests, registrations)
                                enter("Invitatul a fost sters cu succes")
                            except ValueError as error:
                                enter(f"Eroare: {error}")


                    case "modifica":
                        if command[1] == "eveniment":
                            command = " ".join(command)
                            command = command.split(maxsplit=5)
                            try:
                                modify_event(extract_id(command), extract_date(command), extract_time(command), extract_description(command), all_events)
                            except ValueError as error:
                                enter(f"Eroare: {error}")
                            
                        if command[1] == "invitat":
                            try:
                                modify_guest(extract_id(command), extract_name(command), extract_address(command), all_guests)
                            except ValueError as error:
                                enter(f"Eroare: {error}")


                    case "cauta":
                        if command[1] == "eveniment":
                            try:
                                enter(search_event(extract_description(command), all_events))
                            except ValueError as error:
                                enter(f"Eroare: {error}")

                        elif command[1] == "invitat":
                            try:
                                enter(search_guest(extract_name(command), all_guests))
                            except ValueError as error:
                                enter(f"Eroare: {error}")
                        
                        elif command[1] == "invitati":
                            for guest in all_guests:
                                print(guest)
                            enter()
                        
                        elif command[1] == "evenimente":
                            for event in all_events:
                                print(event)
                            enter()


                    case "inscrie":
                        try:
                            guest = getGuestByName(all_guests, extract_name(command))
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
                            event = getEventByDescrpition(all_events, extract_description(command))
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
                            try:
                                registrations.register(guest, event)
                                enter("Inregistrarea a fost facuta cu succes")
                            except ValueError as error:
                                enter(f"Eroare: {error}")


                    case "raport":
                        try:
                            if command[1] == "invitat":
                                for event in registrations.getEventsByGuest(getGuestByName(all_guests, extract_name(command))):
                                    print(event)
                                enter()
                            
                            elif command[1] == "invitati":
                                print_top_guests(registrations)

                            elif command[1] == "evenimente":
                                print_top_20_percent_events(registrations)

                            elif command[1] == "invitati2":
                                print_top_20_percent_guests(all_guests)
                        except ValueError as error:
                            enter(f"Eroare: {error}")
                

                    case "help":
                        help_menu()


                    case "exit":
                        save_events_to_csv("data/events.csv", all_events)
                        save_guests_to_csv("data/guests.csv", all_guests)
                        save_logs_to_csv("data/logs.csv", registrations)
                        exit()


                    case "debug":
                        print(registrations)
                        print("Guests:")
                        for guest in all_guests:
                            print(guest)
                        print("\nEvents:")
                        for event in all_events:
                            print(event)
                        enter()

            except IndexError:
                pass

if __name__ == "__main__":
    main()
