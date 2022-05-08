def hours_per_day(file_name):
    input = open(file_name)
    for line in input:
        line_val = list(line.split())
        line_val[2:] = list(map(float,line_val[2:]))
        time_sum = sum((line_val[2:]))
        print(line_val[1] + " ID <built-in function id> worked " \
              + str(time_sum) + " hours: " + str(time_sum/5) + " / day")

hours_per_day("hours.txt")
