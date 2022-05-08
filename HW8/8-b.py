def input_stats(file_name):
    input = open(file_name)
    max_linelen = 0
    for line in input:
        if len(line) > max_linelen:
            max_linelen = len(line)
            max_line = line
    print("Longest line = " + str(max_linelen))
    print(max_line)

input_stats("hours.txt")

