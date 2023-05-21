from random import choice


def interpret(code):
    output = ''
    stack = []
    moving_char = ''  # going this way till direction is changed
    text_mode = False
    moving_char_table = ['<', '>', '^', 'v']  # possibilities of move
    available_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    available_math_signs = ['+', '-', '*', '/', '%', '`']

    code = code.split('\n')
    code = [[*item] for item in code]
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
            return a + b
        if math_sign == '-':
            return b - a
        if math_sign == '*':
            return a * b
        if math_sign == '/':  # rounded down
            if a == 0:
                return '0'
            return int(b / a)
        if math_sign == '%':
            if a == 0:
                return '0'
            return b % a
        if math_sign == '`':
            if b > a:
                return '1'
            return '0'

    while current_char != '@':
        # print(current_char, stack)
        if code[row][position] == ' ':  # if new char is empty, stay with old one
            row, position = make_a_move(row, position)
            continue
        if current_char == '#':
            row, position = make_a_move(row, position)
        current_char = code[row][position]
        if current_char in moving_char_table:
            moving_char = current_char
        elif current_char == '?':
            moving_char = choice(['<', '>', '^', 'v'])
        elif current_char == '_':
            num1 = stack.pop()
            if num1 == 0:
                moving_char = '>'
            else:
                moving_char = '<'
        elif current_char == '|':
            num1 = stack.pop()
            if num1 == 0:
                moving_char = 'v'
            else:
                moving_char = '^'

        row, position = make_a_move(row, position)

        if current_char in available_digits:
            stack.append(int(current_char))
            continue
        if current_char in available_math_signs:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(make_a_math(num1, num2, current_char))
            continue
        if current_char == '!':
            num1 = stack.pop()
            if num1 == 0:
                stack.append(1)
            else:
                stack.append(0)
            continue
        if current_char == ':':
            if len(stack) == 0:
                stack.append(0)
                continue
            stack.append(stack[-1])
        if current_char == '"':
            text_mode = not text_mode
            continue
        if text_mode:
            stack.append(ord(current_char))
            continue
        if current_char == '\\':
            if len(stack) == 1:
                stack.append(0)
            stack[-2], stack[-1] = stack[-1], stack[-2]
            continue
        if current_char == '$':
            stack.pop()
            continue
        if current_char == '.':
            output += str(stack.pop())  # it is not possible to add integer to string, sorry codewars
            continue
        if current_char == ',':
            output += chr(stack.pop())
            continue
        if current_char == 'p':
            y = stack.pop()
            x = stack.pop()
            v = stack.pop()
            code[y][x] = str(v)
            continue
        if current_char == 'g':
            y = stack.pop()
            x = stack.pop()
            stack.append(ord(code[y][x]))
            continue

    return output
