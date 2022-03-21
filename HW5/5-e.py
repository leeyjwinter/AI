def print_many(message, n=1, outline="*" * 13):
    if not message:
        print(outline)
        return
    for i in range(n):
        print(message)


print_many("")
print_many("Sungkyunkwan", 1)
print_many("SKKU", 3)
print_many("")
