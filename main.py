def interpret(code):
    # output = ''
    stack = []
    moving_char = ''  # going this way till direction is changed
    moving_char_table = ['<', '>', '^', 'v']  # possibilities of move
    avaliable_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    code = code.split('\n')
    row, position = 0, 0
    current_char = code[row][position]

    def make_a_move(row_num, pos_num):
        if moving_char == '>':
            return row_num, pos_num + 1
        if moving_char == '<':
            return row_num, pos_num - 1
        if moving_char == '^':
            return row_num - 1, pos_num
        if moving_char == 'v':
            return row_num + 1, pos_num

    while current_char != '@':
        if code[row][position] == ' ':  # if new char is empty, stay with old one
            continue
        current_char = code[row][position]
        if current_char in moving_char_table:
            moving_char = current_char
        row, position = make_a_move(row, position)

        if current_char in avaliable_digits:
            stack.append(int(current_char))
            continue

    return stack


print(interpret('>112@'))
# print(interpret('>987v>.v\nv456<  :\n>321 ^ _@'))
