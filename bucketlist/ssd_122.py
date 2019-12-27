import sys
import math

def addSquared(numbers):
    sum = 0
    for number in numbers:
        sum += number * number
    return sum

def decimalToBase(number, base):
    result = []
    while number != 0:
        remainder = number % base
        result.append(remainder)
        number = number // base
    return list(reversed(result))

line = sys.stdin
lineCnt = 0
failedLines = []
for a in line:
    lineCnt += 1
    a = a.strip()
    a = a.split()
    try:
        number = int(a[0])
        base = int(a[1])
        print(addSquared(decimalToBase(number, base)))
    except ValueError:
        failedLines.append(lineCnt)
if failedLines:
    print("Failed to convert line(s): ", end='')
    for index in range(len(failedLines)):
        if index == len(failedLines) - 1:
            print(failedLines[index], " ", sep='')
        else:
            print(failedLines[index], ",", sep='', end=' ')
