def create_box(height, width):
    if height == 1:
        print("*" * width)
        return

    print("*" * width)
    for i in range(height - 2):
        print("*" + " " * (width - 2) + "*")
    print("*" * width)


create_box(1, 13)
print()
create_box(1, 7)
print()
create_box(1, 35)
print()
create_box(3, 10)
print()
create_box(4, 5)