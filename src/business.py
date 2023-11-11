import sys
from event import Event
from guest import Guest
from datetime import date, time
from ui import clear

all_guests = []
all_events = []

def execute(command: list):
    match command[0]:
        case "adauga":
            if command[1] == "eveniment":
                year, month, day = list(map(int, command[2].split("-")))
                event_date = date(year, month, day)

                hour, minute = list(map(int, command[3].split(":")))
                event_time = time(hour, minute)

                event_description = ""
                if len(command) == 5:
                    event_description = command[4]

                add_event(all_events, Event(event_date, event_time, event_description))
            
            elif command[1] == "invitat":
                guest_name, guest_address = command[2], command[3]
                add_guest(all_guests, Guest(guest_name, guest_address))

        case "exit":
            clear()
            print("Bye bye")    
            sys.exit()

        case "debug":
            debug()

def add_event(event_list: list, event: "Event"):
    event_list.append(event)

def add_guest(guest_list: list, guest: "Guest"):
    guest_list.append(guest)

def debug():
    print(all_events, all_guests, sep="\n")
