scores_file = open("scores.txt")
scores = []
histogram = []
for line in scores_file:
    scores.append(int(line))

while scores:
    score_val = scores[0]
    score_count = scores.count(scores[0])
    histogram.append((scores[0], score_count))
    while score_val in scores:
        scores.remove(score_val)

histogram.sort(key=lambda x: x[0])
for i in histogram:
    print(i[0], " ", i[1] * "*")
