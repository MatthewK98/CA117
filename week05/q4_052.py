import sys
line = sys.stdin
file = sys.argv[1] 
fridge = {}
output = {}
with open(file, "r") as f:
    for i in f:
        i = i.strip().split()
        food = " ".join(i[:-1])
        calories = i[-1]
        fridge[food] = calories
total = 0
for word in line:
    word = word.strip().split(",")
    name = word[0]
    if len(name) > total:
        total = len(name)
    foods = i[1:]
    total_calories = 0
    for i in foods:
        cal = fridge.get(i)
        if i in fridge:
            total_calories += int(cal)
        else:
            total_calories += 100
    output[name] = total_calories
print(output)