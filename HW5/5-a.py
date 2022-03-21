print("#" + "=" * 16 + "#")
for line in range(4):
    print("|" + " " * (4 - line - 1) * 2 + "<>" + "." * line * 4
          + "<>" + " " * (4 - line - 1) * 2 + "|")
for line in range(3, -1, -1):
    print("|" + " " * (4 - line - 1) * 2 + "<>" + "." * line * 4
          + "<>" + " " * (4 - line - 1) * 2 + "|")
print("#" + "=" * 16 + "#")
