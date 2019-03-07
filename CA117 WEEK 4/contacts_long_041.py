import sys
line = sys.stdin
file = sys.argv[1]
contacts = {}
with open(file, "r") as f:
    for word in f:
        word = word.strip().split()
        name = word[0]
        number = word[1]
        email = word[2]
        info = {}
        info["Number"] = number
        info["Email"] = email
        contacts[name] = info
    for text in line:
        text = text.strip()
        information = contacts.get(text)
        print("Name:", text)
        if information is None:
            print("No such contact")
        else:
            number = information.get("Number")
            email = information.get("Email")
            print("Phone:", number)
            print("Email:", email)
