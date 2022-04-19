input = open("gasprices.txt")
korea = []
japan = []

for line in input:
    line_val = list(line.split())
    japan.append(line_val[0])
    korea.append(line_val[1])

korea = [int(i) for i in korea]
japan = [int(i) for i in japan]

out6 = open("out6.txt","w")
out6.write("Japan average : " +str(sum(japan)/len(japan)) + "\n")
out6.write("Korea average   : " + str(sum(korea)/len(korea)) + "\n")

