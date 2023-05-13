def interpret(code):
    output = ''
    stack = []
    moving_char = ''
    moving_char_table = []

    code = code.split('\n')
    row, position = 0, 0
    current_char = code[row][position]

    def make_a_move(row, position):
        if moving_char == '>':
            return row, position + 1
        if moving_char == '<':
            return row, position - 1
        if moving_char == '^':
            return row - 1, position
        if moving_char == 'v':
            return row + 1, position

    while current_char != '@':
        make_a_move(row, position)
        if code[row][position] == ' ':  # if new char is empty, stay with old one
            continue
        else:
            current_char = code[row][position]
        if type(current_char) == int:
            stack.insert(-1, current_char)
            continue
        if current_char in moving_char_table:
            moving_char = current_char
            continue

    return stack


print(interpret('1,1,2,@'))
# print(interpret('>987v>.v\nv456<  :\n>321 ^ _@'))
