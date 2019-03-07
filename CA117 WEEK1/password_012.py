import sys
from string import punctuation
line = sys.stdin
for a in line:
    number = 0
    upper = 0
    lower = 0
    punc = 0
    for i in a:
        if i.isdigit():
            number = 1
        if i.isupper():
            upper = 1
        if i.islower():
            lower = 1
        if i in punctuation:
            punc = 1
    print(number + upper + lower + punc)
# import sys
# from string import punctuation

# def main():
#     for line in sys.stdin:
#         lowers = 0
#         uppers = 0
#         digits = 0
#         specials = 0
#         for i in line.strip():
#             if i.islower():
#                 lowers = 1
#             if i.isupper():
#                 uppers = 1
#             if i.isdigit():
#                 digits = 1
#             if i in punctuation:
#                 specials = 1
#         print(sum([lowers, uppers, digits, specials]))
        
# if __name__ == '__main__':
#     main()