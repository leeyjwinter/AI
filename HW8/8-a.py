from random import *


def rand_dice_sum():
    first_num = randint(1, 6)
    second_num = randint(1, 6)
    result_num = first_num + second_num
    print(str(first_num) + " + " + str(second_num) + " = " + str(result_num))
    return result_num


cnt = 0
while True:
    if rand_dice_sum() == 7:
        cnt += 1
        break
    else:
        cnt += 1

print("You won after " + str(cnt) + " tries!!!111~")
