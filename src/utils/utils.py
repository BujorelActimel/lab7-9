import datetime

def id_input(msg=""):
    while True:
        try:
            id_ = int(input(f"{msg}ID: ").strip())
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

def raport_input():
    while True:
        try:
            raport = int(input("Raport: ").strip())
        except ValueError:
            print("Raport must be an integer.")
        if raport not in range(1, 4):
            print("Invalid raport.")
            continue
        return raport

def enter(msg=""):
    input(f"{msg}Press ENTER to continue.")

def quicksort(arr, key=lambda x: x, reverse=False):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if key(x) < key(pivot)]
        middle = [x for x in arr if key(x) == key(pivot)]
        right = [x for x in arr if key(x) > key(pivot)]
        if reverse:
            return quicksort(right, key, reverse) + middle + quicksort(left, key, reverse)
        else:
            return quicksort(left, key, reverse) + middle + quicksort(right, key, reverse)

def gnome_sort(arr, key=lambda x: x, reverse=False, index=0):
    if index >= len(arr) - 1:
        return arr if not reverse else arr[::-1]
    if key(arr[index]) > key(arr[index + 1]):
        arr[index], arr[index + 1] = arr[index + 1], arr[index]
        if index > 0:
            return gnome_sort(arr, key, reverse, index - 1)
    return gnome_sort(arr, key, reverse, index + 1)
