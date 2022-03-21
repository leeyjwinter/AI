HALF_LINE = 4


def drawer():
    print("#" + "=" * 16 + "#")
    for line in list(range(HALF_LINE)) + list(range(HALF_LINE - 1, -1, -1)):
        print("|" + " " * (HALF_LINE - line - 1) * 2 + "<>" + "." * line * HALF_LINE
              + "<>" + " " * (HALF_LINE - line - 1) * 2 + "|")
    print("#" + "=" * 16 + "#")


drawer()
