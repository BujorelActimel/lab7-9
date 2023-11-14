import os
import sys
from datetime import date, time

succes_messages = [
    "Evenimentul a fost adaugat cu succes",
    "Invitatul a fost adaugat cu succes",
    "bye bye",
    "debug",
]


def clear():
    os.system("cls")


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


def debug(guest_list: list, event_list: list):
    print(guest_list, event_list, sep="\n")


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
        return "Enter"

    if len(command) < 3 and command[0] not in valid_commands:
        return "Prea putine argumente"

    if command[0] not in valid_commands:
        return "Primul argument este invalid"

    match command[0]:
        case "adauga":
            if command[1] == "eveniment":
                if len(command) < 4:
                    return "Prea putine argumente"

                if not valid_date(command[2]):
                    return "Data evenimentului este invalida"

                if not valid_time(command[3]):
                    return "Timpul evenimentului este invalid"

                if len(command) == 5 and not valid_description(command[4]):
                    return "Descrierea evenimentului este invalida"
                
                return "Evenimentul a fost adaugat cu succes"
            
            elif command[1] == "invitat":
                if len(command) < 4:
                    return "Prea putine argumente"

                return "Invitatul a fost adaugat cu succes"

            else:
                return "Al doilea argument este invalid"
        
        case "exit":
            return "bye bye"

        case "debug":
            return "debug"


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
