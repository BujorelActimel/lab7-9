import datetime

def id_input():
    while True:
        try:
            id_ = int(input("ID: "))
            return id_
        except ValueError:
            print("ID must be an integer.")
            continue

def name_input(update=False):
    while True:
        name = input("Name: ").strip()
        if name == "" and not update:
            print("Name cannot be empty.")
            continue
        return name

def address_input(update=False):
    while True:
        address = input("Address: ").strip()
        if address == "" and not update:
            print("Address cannot be empty.")
            continue
        return address

def date_input(update=False):
    while True:
        try:
            date = input("Date (YYYY-MM-DD): ").strip()
            if date == "" and update:
                return date
            datetime.datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format.")
            continue

def time_input(update=False):
    while True:
        try:
            time = input("Time (HH:MM): ").strip()
            if time == "" and update:
                return time
            datetime.datetime.strptime(time, "%H:%M")
            return time
        except ValueError:
            print("Invalid time format.")
            continue

def description_input(update=False):
    while True:
        description = input("Description: ").strip()
        if description == "" and not update:
            print("Description cannot be empty.")
            continue
        return description

def enter(msg=""):
    input(f"{msg} Press ENTER to continue.")
