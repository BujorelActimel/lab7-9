import os
import sys
from datetime import date, time

def clear():
    os.system("cls")


def enter(msg):
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

            else:
                raise ValueError("Al doilea argument este invalid")

        case "inscrie":
            if len(command) < 3:
                raise ValueError("Prea putine argumente")
            
            if type(command[1]) != str:
                raise ValueError("Primul argument este invalid")

            if type(command[2]) != str:
                raise ValueError("Al doilea argument este invalid")

            command[2]

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
    year, month, day = list(map(int, command[2].split("-")))
    return date(year, month, day)


def extract_time(command: list):
    hour, minute = list(map(int, command[3].split(":")))
    return time(hour, minute)


def extract_description(command: list):
    event_description = ""
    if len(command) == 5:
        event_description = command[4]
    return event_description


def extract_name(command: list):
    return command[2]


def extract_address(command: list):
    return " ".join(command[3:])


def exit():
    clear()    
    sys.exit("Bye bye")
