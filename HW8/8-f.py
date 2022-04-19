import copy

movie_file = open("movies.txt")
movies = []
result = []
for line in movie_file:
    line_val = list(line.split(" "))
    line_val[3] = " ".join(line_val[3:])
    line_val[3] = line_val[3].strip("\n")
    line_val = line_val[:4]
    movies.append(line_val)

lower_movies = copy.deepcopy(movies)
for lists in lower_movies:
    lists[3] = lists[3].lower()

print("Search word? ", end="")
search_word = input().lower()

for i in range(4):
    matching = [lower_movies.index(s) for s in lower_movies if search_word in s[i]]
    result.extend(matching)

result.sort()

for index in result:
    index = movies[index]
    print(index[0], "\t", index[2], "\t", index[1], "\t", index[3])
print(str(len(result))+" matches.")
