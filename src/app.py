from ui import AppUI
from repository import Repo

def main():
    repository = Repo(
        "../data/events.csv", 
        "../data/guests.csv", 
        "../data/logs.csv",
    )
    app = AppUI(repository)
    app.mainloop()

if __name__ == '__main__':
    main()
