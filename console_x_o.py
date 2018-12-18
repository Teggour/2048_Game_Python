field_of_play = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
symb_x = 'X'
symb_o = 'O'

def show_field(field_of_play):
    print("\n" + " ---   ---   ---")

    for i in range(len(field_of_play)):
        for j in range(len(field_of_play[i])):
            print("|", field_of_play[i][j], end=" | ")

        if i != range(len(field_of_play)):
            print("\n" + " ---   ---   ---")


def change_field(field_of_play, choice, symb):
    for i in range(len(field_of_play)):
        for j in range(len(field_of_play[i])):
            if choice is field_of_play[i][j]:
                field_of_play[i][j] = symb
                break

'''Check'''
def check(field_of_play, ch):
    '''Check in line'''
    for i in range(len(field_of_play)):
        for j in range(len(field_of_play[i])):
            if len(set(field_of_play[i])) == 1:
                print("!!!! WIN !!!!")
                ch = False
                return ch

    '''Check in column'''
    for i in range(len(field_of_play)):
        c = []
        for j in range(len(field_of_play[i])):
            c.append(field_of_play[j][i])

        if len(set(c)) == 1:
            print("!!!! WIN !!!!")
            ch = False
            return ch

    '''Check in diagonal 1'''
    x = []
    for i in range(len(field_of_play)):
        x.append(field_of_play[i][i])

    if len(set(x)) == 1:
        print("!!!! WIN !!!!")
        ch = False
        return ch

    '''Check in diagonal 2'''
    z = []
    j = len(field_of_play) - 1

    for i in range(len(field_of_play)):
        z.append(field_of_play[i][j])
        j -= 1

    if len(set(z)) == 1:
        print("!!!! WIN !!!!")
        ch = False
        return ch


show_field(field_of_play)

ch = True

for i in range(9):
    choice = input("Choice field: ")

    if i % 2 == 0:
        change_field(field_of_play, choice, symb_x)
    else:
        change_field(field_of_play, choice, symb_o)

    show_field(field_of_play)

    if i > 3:
        ch = check(field_of_play, ch)
        if ch is False:
            break
