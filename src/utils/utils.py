import datetime

def id_input():
    while True:
        try:
            id_ = int(input("ID: "))
            return id_
        except ValueError:
            print("ID must be an integer.")
            continue

def name_input():
    while True:
        name = input("Name: ")
        if name == "":
            print("Name cannot be empty.")
            continue
        return name

def address_input():
    while True:
        address = input("Address: ")
        if address == "":
            print("Address cannot be empty.")
            continue
        return address

def date_input():
    while True:
        try:
            date = input("Date (YYYY-MM-DD): ")
            datetime.datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format.")
            continue

def time_input():
    while True:
        try:
            time = input("Time (HH:MM): ")
            datetime.datetime.strptime(time, "%H:%M")
            return time
        except ValueError:
            print("Invalid time format.")
            continue

def description_input():
    while True:
        description = input("Description: ")
        if description == "":
            print("Description cannot be empty.")
            continue
        return description

def enter(msg=""):
    input(f"{msg} Press ENTER to continue.")
