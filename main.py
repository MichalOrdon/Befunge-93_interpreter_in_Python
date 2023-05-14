from random import choice

def interpret(code):
    output = ''
    stack = []
    moving_char = ''  # going this way till direction is changed
    moving_char_table = ['<', '>', '^', 'v']  # possibilities of move
    available_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    available_math_signs = ['+', '-', '*', '/', '%', '`']

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

    def make_a_math(a, b, math_sign):
        if math_sign == '+':
            return str(a + b)
        if math_sign == '-':
            return str(b - a)
        if math_sign == '*':
            return str(a * b)
        if math_sign == '/':  # rounded down
            if a == 0:
                return '0'
            return str(int(b / a))
        if math_sign == '%':
            if a == 0:
                return '0'
            return str(b % a)
        if math_sign == '`':
            if b > a:
                return '1'
            return '0'

    while current_char != '@':
        if code[row][position] == ' ':  # if new char is empty, stay with old one
            continue
        current_char = code[row][position]
        if current_char in moving_char_table:
            moving_char = current_char
        elif current_char == '?':
            moving_char = choice(['<', '>', '^', 'v'])
        row, position = make_a_move(row, position)

        if current_char in available_digits:
            stack.append(int(current_char))
            continue
        if current_char in available_math_signs:
            num1 = stack.pop()
            num2 = stack.pop()
            output += make_a_math(num1, num2, current_char)
            continue
        if current_char == '!':
            num1 = stack.pop()
            if num1 == 0:
                output += '1'
            else:
                output += '0'
            continue

    return output


# print(interpret('>?@'))
# print(interpret('>987v>.v\nv456<  :\n>321 ^ _@'))
