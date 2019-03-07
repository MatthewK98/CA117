import sys
line = sys.stdin
file = sys.argv[1]
contacts = {}
with open(file, "r") as f:
    for word in f:
        word = word.strip()
        word = word.split()
        name = word[0]
        number = word[1]
        contacts[name] = number
    for text in line:
        text = text.strip()
        number = contacts.get(text)
        print("Name:", text)
        if text in contacts:
            print("Phone:", number)
        else:
            print("No such contact")
