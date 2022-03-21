print("#" + "=" * 16 + "#")
for line in list(range(4)) + list(range(3, -1, -1)):
    print("|" + " " * (4 - line - 1) * 2 + "<>" + "." * line * 4
          + "<>" + " " * (4 - line - 1) * 2 + "|")

print("#" + "=" * 16 + "#")
