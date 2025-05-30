def readf():
    with open("notes.txt","r") as file:
        content=file.read()
        print("\n"+content)

def add_to_file():
    more_note=input("Enter notes to add")
    with open("notes.txt","a") as file:
        file.write(more_note+"\n")
        print("Note saved")

def main():
    while True:
        print("Welcome to note writing app")
        print("Enter 1 to write a note")
        print("Enter 2 to see a notes")
        print("Enter 3 to exit")

        n=int(input("Enter your choice"))

        if n==1:
            add_to_file()
        elif n==2:
            readf()
        elif n==3:
            print("App exited")
            break
        else:
            print("Wrong choice try again")
main()