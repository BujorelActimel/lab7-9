# comenzi:
#     - adauga, sterge, modifica, cauta:
#         eveniment
#         invitat
#     - inscrie invitat la un eveniment
from ui import *
from business import *

def main():
    all_guests = []
    all_events = []
    while True:
        print_menu()
        command = get_command()

        validation_message = validate_command(command)
        
        if validation_message in succes_messages:
            match command[0]:
                case "adauga":
                    if command[1] == "eveniment":
                        add_event(extract_date(command), extract_time(command), extract_description(command), all_events)
                    
                    elif command[1] == "invitat":
                        add_guest(extract_name(command), extract_address(command), all_guests)

                case "exit":
                    exit()

                case "debug":
                    debug(all_guests, all_events)

        input(f"{validation_message}\nPress Enter to continue")

if __name__ == "__main__":
    main()
