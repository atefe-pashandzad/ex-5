class Contact:
    def __init__(self, name, phone):
    
        for ch in phone:
            if ch not in "0123456789":
                raise ValueError ("namotbr")
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name} - {self.phone}"
contacts = []

while True:
    print("meno")
    print("add contact")
    print("show")
    print("save exit")

    try:
        option = int(input(" choise "))
    except ValueError:
        print("enter num")
        continue

    if option == 1:
        while True:
            n = input("name")
            p = input("shomare")
            try:
                c = Contact(n, p)
                contacts.append(c)
                print("add shd contact")
                break
            except ValueError:
                print("wrong wared krd")

    elif option == 2:
        if contacts:
            print("list")
            for c in contacts:
                print(c)
        else:
            print("empty l")

    elif option == 3:
        with open("contacts.txt", "w", encoding="utf-8") as f:
            for c in contacts:
                f.write(str(c) + "\n")
        print("sav")
        break

    else:
        print("namish")
