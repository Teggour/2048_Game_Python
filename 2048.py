import random

field = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]


def show_field(field):
    print("\n" + " ---   ---   ---   ---")

    for i in range(len(field)):
        for j in range(len(field[i])):
            print("|", field[i][j], end=" | ")

        if i != range(len(field)):
            print("\n" + " ---   ---   ---   ---")


def move_up(field):
    for k in range(len(field)):
        for i in range(len(field) - 1):
            for j in range(len(field[i])):
                if field[i][j] == 0 and field[i+1] != 0:
                    field[i][j] = field[i+1][j]
                    field[i+1][j] = 0


def sum_up(field):
    for i in range(len(field)-1):
        for j in range(len(field[i])):
            if field[i][j] == field[i+1][j] and field[i][j] != 0:
                field[i][j] = field[i][j] + field[i+1][j]
                field[i+1][j] = 0
                move_up(field)


def move_down(field):
    for k in range(len(field)):
        for i in range(len(field)-1):
            for j in range(len(field[i])):
                if field[i+1][j] == 0:
                    field[i+1][j] = field[i][j]
                    field[i][j] = 0


def sum_down(field):
    for i in range(len(field)-1, -1, -1):
        for j in range(len(field[i])):
            if field[i-1][j] == field[i][j] and field[i][j] != 0:
                field[i][j] = field[i][j] + field[i-1][j]
                field[i-1][j] = 0
                move_down(field)


def move_left(field):
    for k in range(len(field)):
        for i in range(len(field)-1):
            for j in range(len(field[i])):
                if field[j][i] == 0 and field[j][i+1] != 0:
                    field[j][i] = field[j][i+1]
                    field[j][i+1] = 0


def sum_left(field):
    for i in range(len(field)-1):
        for j in range(len(field[i])):
            if field[j][i] == field[j][i+1]:
                field[j][i] = field[j][i] + field[j][i+1]
                field[j][i+1] = 0
                move_left(field)


def move_right(field):
    for k in range(len(field)):
        for i in range(len(field)-1):
            for j in range(len(field[i])):
                if field[j][i+1] == 0 and field[j][i] != 0:
                    field[j][i+1] = field[j][i]
                    field[j][i] = 0


def sum_right(field):
    for i in range(len(field)-1, -1, -1):
        for j in range(len(field[i])):
            if field[j][i] == field[j][i-1]:
                field[j][i] = field[j][i] + field[j][i-1]
                field[j][i-1] = 0
                move_right(field)


def move(choice, field):
    if choice == "s":
        move_down(field)
        sum_down(field)

    elif choice == "w":
        move_up(field)
        sum_up(field)

    elif choice == "a":
        move_left(field)
        sum_left(field)

    elif choice == "d":
        move_right(field)
        sum_right(field)


def rand_generator():
    rnd_i = random.randint(0, 2)
    rnd_j = random.randint(0, 2)
    return rnd_i, rnd_j


for i in range(2):
    rnd_i, rnd_j = rand_generator()
    field[rnd_i][rnd_j] = 3

ch = True

while ch is True:
    show_field(field)

    choice = input("Move (w,a,s,d): ")
    move(choice, field)
    show_field(field)

    check = True

    while check:
        rnd_i, rnd_j = rand_generator()
        if field[rnd_i][rnd_j] == 0:
            field[rnd_i][rnd_j] = 3
            check = False

    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 96:
                ch = False
