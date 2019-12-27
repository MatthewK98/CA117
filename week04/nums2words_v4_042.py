import sys
line = sys.stdin
first_twenty = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tenths = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "one hundred"]
add_ons = ["", "-one", "-two", "-three", "-four", "-five", "-six", "-seven", "-eight", "-nine"]
for i in line:
    i = i.strip()
    i = i.split()
    line = ""
    for a in i:
        a = int(a)
        if a <= 19:
            line += first_twenty[a] + " "
        else:
            a = str(a)  # Reason for using str rather than int , is because "int" object is not iterable
            a = list(a)
            first = int(a[0]) - 2
            second = int(a[1])
            line += tenths[int(first)] + add_ons[int(second)] + " "
    print(line.strip())
