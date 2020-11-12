def row_win(x_win, o_win):
    for i in range(3):
        if user_pos[i + 0] == user_pos[i + 1] == user_pos[i + 2] == "X":
            x_win = 1
        if user_pos[i + 0] == user_pos[i + 3] == user_pos[i + 6] == "X":
            x_win = 1
    if user_pos[0] == user_pos[4] == user_pos[8] == "X":
        x_win = 1
    if user_pos[2] == user_pos[4] == user_pos[6] == "X":
        x_win = 1
    for i in range(3):
        if user_pos[i + 0] == user_pos[i + 1] == user_pos[i + 2] == "O":
            o_win = 1
        if user_pos[i + 0] == user_pos[i + 3] == user_pos[i + 6] == "O":
            o_win = 1
    if user_pos[0] == user_pos[4] == user_pos[8] == "O":
        o_win = 1
    if user_pos[2] == user_pos[4] == user_pos[6] == "O":
        o_win = 1
    return x_win, o_win


def print_field():
    print("---------")
    print("|", user_pos[0], user_pos[1], user_pos[2], "|")
    print("|", user_pos[3], user_pos[4], user_pos[5], "|")
    print("|", user_pos[6], user_pos[7], user_pos[8], "|")
    print("---------")


def correct_begin():
    imp = 0
    if win == (1, 1):
        imp = 1
    elif abs(user_pos.count("X") - user_pos.count("O")) > 1:
        imp = 1
    if imp == 1:
        print("Impossible")
    elif win == (1, 0):
        print("X wins")
    elif win == (0, 1):
        print("O wins")
    elif win == (0, 0):
        if user_pos.count("_") > 0 or user_pos.count(" ") > 0:
            print("Game not finished")
        else:
            print("Draw")

def test_user_coord(user_coord_in):
    good_digit = ["1", "2", "3"]
    if user_coord_in[0].isdigit() and user_coord_in[1].isdigit():
        print("good")
    bad_value_in = [value for value in user_coord_in if value not in good_digit]




user_pos = input("Enter cells:")
x_win = 0
o_win = 0
win_in = 0

win = row_win(0, 0)

print_field()
# correct_begin()
while win_in == 0:
    user_coord_in = input("Enter the coordinates:").split()
    print(user_coord_in)
    test_user_coord(user_coord_in)

