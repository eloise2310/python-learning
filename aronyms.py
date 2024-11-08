def find_acronym():
    look_up = input("What software acronym would you like to look up?\n").strip().upper()  # Normalize input to uppercase
    found = False
    try:
        with open("acronym.txt") as file:
            for line in file:
                if look_up in line.upper():  # Exact match with the acronym
                    print(line)
                    found = True
                    break
    except FileNotFoundError:
        print("Error: File not found.")
        return
    if not found:
        print("The acronym does not exist")

def add_acronym():
    acronym = input("What acronym do you want to add?\n").strip().upper()  # Normalize input
    definition = input("What is the definition?\n").strip()
    with open("acronym.txt", "a") as file:
        file.write(f"{acronym} - {definition}\n")

def main():
    # Ask user if they want to find or add an acronym 
    choice = input("Do you want to find or add an acronym? (Type 'find' or 'add')\n").strip().lower()
    if choice == "find":
        find_acronym()
    elif choice == "add":
        add_acronym()
    else:
        print("Invalid choice. Please type 'find' or 'add'.")

main()
