# comenzi:
#     - adauga, sterge, modifica, cauta:
#         eveniment
#         invitat
#     - inscrie invitat la un eveniment
from ui import *
from business import *

def main():
    while True:
        print_menu()
        command = get_command()
        validation_message = validate_command(command)
        if validation_message in succes_messages:
            execute(command)

        input(f"{validation_message}\nPress Enter to continue")

if __name__ == "__main__":
    main()
