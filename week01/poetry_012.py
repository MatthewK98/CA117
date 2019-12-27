import sys
song = []
longest = 0
for line in sys.stdin:      # for each line on input
    line = line.strip()       # remove trailing newspace
    if len(line) > longest:  # and if the line is currently the longest one
        longest = len(line)  # set longest integer to the length of the line
    song.append(line)       # save the line into list, so we can print it later

for line in song:           # for each line in the song
    print('{text:^{width}}'.format(text=line, width=longest))
    # this is a tricky one
    # print('{text}'.format(text=line)) prints line as print(line) would
    # print('{text:20}'.format(text=line)) says there is 20 characters of space for line,
    # if line is shorter, then it puts " " in front
    # print('{text:^20}'.format(text=line)) the same, but line is now centered, not on the right
    # however, we need the width set to variable, se we do exactly that
    # print('{text:^{width}}'.format(text=line, width=longest)) thats how we get this
    # more about this kind of formatting at: https://pyformat.info/
    # shorter:
    # print('{text}'.format(text=variable))  prints variable
    # :20 sets width to 20 chars
    # :^ centers the textb vb
