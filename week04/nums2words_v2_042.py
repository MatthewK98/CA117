import sys
line = sys.stdin
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
for a in line:
    a = a.strip()
    a = a.split()
    line = ""
    for i in a:
        if i.isnumeric() and int(i) in range(11):
            line += numbers[int(i)] + " "
        else:
            line += "unknown" + " "
    print(line.strip())
