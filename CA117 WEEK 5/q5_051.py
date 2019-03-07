import sys
line = sys.stdin
dict = {}
def seconds(s):
    s = s.strip()
    s = s.split(":")
    minute = s[0]
    seconds = s[1]
    total = int(minute) * 60 + int(seconds)
    return total
def convert_back(s):
    min = s // 60
    sec = s % 60
    return "{}:{:02}".format(min, sec)
for word in line:
    word =  word.strip().split()
    name = word[0]
    numbers = word[1:]
    time = []
    for char in numbers:
        try:
            time.append(seconds(char))
        except:
            break
    dict[name] = min(time)
lowest = sorted((value, key) for (key,value) in dict.items())[0]
print(lowest[1], ":", convert_back(lowest[0]))
