import sys

def build_dictionary(filename):
    Keys_Vals = {}
    with open(filename, "r") as f:
        for word in f:
            word = word.split()
            key = word[0]
            value = word[1]
            Keys_Vals[key] = value
        return Keys_Vals
def extract_range(d, low, high):
    values = d.items()
    q = []
    for i in values:
        q += (i,)
    items = q
    i = 0
    new_dict = {}
    while i < len(items):
        if low <= int(items[i][1]) <= high:
            new_dict[items[i][0]] = items[i][1]
            i = i + 1
        else:
            i = i + 1
    return new_dict
def main():
    d = q3_052.build_dictionary("mappings_052.txt")
    nd = q3_052.extract_range(d, 5, 15)
    for (k, v) in sorted(nd.items()):
      print("{} : {}".format(k, v))
if __name__ == '__main__':
    main()
