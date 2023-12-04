import os
import sys
from datetime import date, time

def clear():
    os.system("cls")


def enter(msg=""):
    input(f"{msg}\nPress Enter to continue")


def print_menu():
    clear()
    print("""Comenzi:
    - adauga (eveniment/invitat)
    - sterge (eveniment/invitat)
    - modifica (eveniment/invitat)
    - cauta (eveniment/invitat)
    - inscrie (invitat la un eveniment)
    - retrage (invitat de la un eveniment)
    - raport (invitat)
    - help
    - exit
    """)


def get_command():
    return input(">>> ").split(maxsplit=4)


def validate_command(command: list):
    valid_commands = [
        "adauga", 
        "sterge", 
        "modifica", 
        "cauta", 
        "inscrie",
        "retrage",
        "raport",
        "help",
        "exit",
        "debug",
    ]

    if len(command) == 0:
        return

    if len(command) < 3 and command[0] not in valid_commands:
        raise ValueError("Prea putine argumente")

    if command[0] not in valid_commands:
        raise ValueError("Primul argument este invalid")

    match command[0]:
        case "adauga":
            if command[1] == "eveniment":
                if len(command) < 4:
                    raise ValueError("Prea putine argumente")

                if not valid_date(command[2]):
                    raise ValueError("Data evenimentului este invalida")

                if not valid_time(command[3]):
                    raise ValueError("Timpul evenimentului este invalid")

                if len(command) == 5 and not valid_description(command[4]):
                    raise ValueError("Descrierea evenimentului este invalida")
                
                enter("Evenimentul a fost adaugat cu succes")
            
            elif command[1] == "invitat":
                if len(command) < 4:
                    raise ValueError("Prea putine argumente")

                enter("Invitatul a fost adaugat cu succes")
            
            elif command[1] == "random":
                if len(command) > 3:
                    raise ValueError("Prea multe argumente")

                if command[2] not in ["invitat", "eveniment"]:
                    raise ValueError("Al treilea argument invalid")

                enter("Invitatul random a fost adaugat cu succes")

            else:
                raise ValueError("Al doilea argument este invalid")
        
        case "sterge":
            if command[1] == "eveniment":
                if len(command) < 3:
                    raise ValueError("Prea putine argumente")
                if not valid_description(" ".join(command[2:])):
                    raise ValueError("Descrierea evenimentului este invalida")
            
            elif command[1] == "invitat":
                if len(command) < 3:
                    raise ValueError("Prea putine argumente")
            
            else:
                raise ValueError("Al doilea argument este invalid")

        case "modifica":
            if command[1] == "eveniment":
                command = " ".join(command)
                command = command.split(maxsplit=5)

                if len(command) < 6:
                    raise ValueError("Prea putine argumente")

                if not valid_date(command[3]):
                    raise ValueError("Data evenimentului este invalida")

                if not valid_time(command[4]):
                    raise ValueError("Timpul evenimentului este invalid")

                if not valid_description(extract_description(command)):
                    raise ValueError("Descrierea evenimentului este invalida")
                
                enter("Evenimentul a fost modificat cu succes")
            
            elif command[1] == "invitat":
                if len(command) < 5:
                    raise ValueError("Prea putine argumente")
                
                enter("Invitatul a fost modificat cu succes")
            
            else:
                raise ValueError("Al doilea argument este invalid")

        case "cauta":
            if command[1] == "eveniment":
                if len(command) < 3:
                    raise ValueError("Prea putine argumente")
                
                if not valid_description(extract_description(command)):
                    raise ValueError("Descrierea evenimentului este invalida")
            
            elif command[1] == "invitat":
                if len(command) < 3:
                    raise ValueError("Prea putine argumente")
            
            elif command[1] == "invitati":
                if len(command) > 2:
                    raise ValueError("Prea multe argumente")
            
            elif command[1] == "evenimente":
                if len(command) > 2:
                    raise ValueError("Prea multe argumente")
            
            else:
                raise ValueError("Al doilea argument este invalid")

        case "inscrie":
            if len(command) < 3:
                raise ValueError("Prea putine argumente")

        case "raport":
            if len(command) < 2:
                raise ValueError("Prea putine argumente")
            
            if command[1] not in ["invitat", "invitati", "evenimente", "invitati2"]:
                raise ValueError("Al doilea argument este invalid")

        case "exit":
            pass

        case "debug":
            pass


def valid_date(input_date: str):
    input_date = input_date.split("-")
    try:
        year, month, day = list(map(int, input_date))
    except:
        return False

    try:
        date(year, month, day)
    except:
        return False
    
    return True


def valid_time(input_time: str):
    input_time = input_time.split(":")

    try:
        hour, minute = list(map(int, input_time))
    except:
        return False
    
    try:
        time(hour, minute)
    except:
        return False

    return True


def valid_description(input_description: str):
    if len(input_description) > 1:
        return input_description[0] == input_description[-1] == "'"
    else:
        return False


def extract_date(command: list):
    if command[0] == "adauga":
        year, month, day = list(map(int, command[2].split("-")))
        return date(year, month, day)
    elif command[0] == "modifica":
        year, month, day = list(map(int, command[3].split("-")))
        return date(year, month, day)


def extract_id(command: list):
    return command[2]


def extract_time(command: list):
    if command[0] == "adauga":
        hour, minute = list(map(int, command[3].split(":")))
        return time(hour, minute)

    elif command[0] == "modifica":
        hour, minute = list(map(int, command[4].split(":")))
        return time(hour, minute)


def extract_description(command: list):
    event_description = ""
    if command[0] == "modifica":
        event_description = " ".join(command[5:])
    elif command[0] == "adauga" and len(command) == 5:
        event_description = " ".join(command[4:])
    elif command[0] == "sterge" or command[0] == "cauta" or command[0] == "inscrie":
        event_description = " ".join(command[2:])
    return event_description


def extract_name(command: list):
    if command[0] == "adauga" or command[0] == "sterge" or command[0] == "cauta" or command[0] == "raport":
        return command[2]
    elif command[0] == "modifica":
        return command[3]
    elif command[0] == "inscrie":
        return command[1]


def extract_address(command: list):
    if command[0] == "adauga":
        return " ".join(command[3:])
    elif command[0] == "modifica":
        return " ".join(command[4:])


def print_top_guests(registration_log):
    enter(registration_log.getGuestsByMostEvents())


def print_top_20_percent_events(registration_log):
    enter(registration_log.getEventsByMostGuests())


def print_top_20_percent_guests(registration_log):
    enter(registration_log.getGuestsByMostEvents()[:int(len(registration_log.getGuestsByMostEvents())*0.2)])


def help_menu():
    clear()
    enter(r"""Comenzi Valabile:
    adauga eveniment {data eveniment} {timp eveniment} {descriere eveniment}
        - data eveniment: an-luna-zi
        - timp eveniment: ora:minut
        - descriere eveniment: 'descr'
    adauga invitat {nume invitat} {adresa eveniment}

    modifica eveniment {id eveniment} {data eveniment} {timp eveniment} {descriere eveniment}
    modifica invitat {id invitat} {nume invitat} {adresa eveniment}

    sterge eveniment {descriere eveniment}
    sterge invitat {nume invitat}

    cauta eveniment {descriere eveniment}
    cauta invitat {nume invitat}
    cauta evenimente
    cauta invitati

    inscrie {nume invitat} {descriere eveniment}

    raport invitat {nume invitat}
    raport invitati
    raport evenimente

    help
    debug
    exit
    """)


def exit():
    clear()    
    sys.exit("Bye bye")
