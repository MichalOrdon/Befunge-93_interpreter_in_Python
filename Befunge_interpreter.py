from random import choice

text_mode = False


def interpret(code):
    global text_mode
    output = ''
    stack = []
    moving_char = '>'  # going this way till direction is changed
    moving_char_table = ['<', '>', '^', 'v']  # possibilities of move
    available_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    available_math_signs = ['+', '-', '*', '/', '%', '`']
    available_output_chars = ['.', ',']
    available_modifying_stack_chars = ['!', ':', '\\', '$', 'g']
    available_changing_direction_chars = ['?', '_', '|']

    code = code.split('\n')
    code = [[*item] for item in code]
    row, position = 0, 0
    current_char = code[row][position]

    def make_move_direction(to_current_char, to_stack):
        if to_current_char == '?':
            return choice(['<', '>', '^', 'v']), to_stack
        if to_current_char == '_':
            num = to_stack.pop()
            if num == 0:
                return '>', to_stack
            else:
                return '<', to_stack
        if to_current_char == '|':
            num = to_stack.pop()
            if num == 0:
                return 'v', to_stack
            else:
                return '^', to_stack

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

    def make_stack(to_stack, to_current_char):
        if to_current_char == '!':
            # print(stack, current_char)
            num = to_stack.pop()
            if num == 0:
                to_stack.append(1)
            else:
                to_stack.append(0)
            # print(stack, current_char)
            return to_stack
        if to_current_char == ':':
            if len(to_stack) == 0:
                to_stack.append(0)
                return to_stack
            to_stack.append(to_stack[-1])
            return to_stack
        if to_current_char == '\\':
            if len(to_stack) == 1:
                to_stack.append(0)
            to_stack[-2], to_stack[-1] = to_stack[-1], to_stack[-2]
            return to_stack
        if to_current_char == '$':
            to_stack.pop()
            return to_stack
        if to_current_char == 'g':
            y_pos = to_stack.pop()
            x_pos = to_stack.pop()
            to_stack.append(ord(code[y_pos][x_pos]))
            return to_stack

    def make_output(to_output, to_stack, char):
        if char == '.':
            to_output += str(to_stack.pop())  # it is not possible to add integer to string, sorry codewars
            return to_output, to_stack
        if char == ',':
            to_char = to_stack.pop()
            if to_char == 10:
                to_output += '\n'
            else:
                if type(to_char) == int:
                    to_output += chr(to_char)
                else:
                    to_output += to_char
            return to_output, to_stack

    while current_char != '@':
        if code[row][position] == ' ' and current_char != '#' and not text_mode:  # if new char is empty, stay with old one
            if text_mode:
                stack.append(' ')
            row, position = make_a_move(row, position)
            continue
        if current_char == '#':
            row, position = make_a_move(row, position)
        current_char = code[row][position]

        # making a move
        if current_char in moving_char_table:
            moving_char = current_char
        if current_char in available_changing_direction_chars:
            moving_char, stack = make_move_direction(current_char, stack)

        row, position = make_a_move(row, position)

        # adding digits to stack
        if current_char in available_digits:
            stack.append(int(current_char))
            continue

        # making math on stack
        if current_char in available_math_signs:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(make_a_math(num1, num2, current_char))
            continue

        # launching text mode
        if current_char == '"':
            text_mode = not text_mode
            continue
        if text_mode:
            stack.append(ord(current_char))
            continue

        # operating on a stack
        if current_char in available_modifying_stack_chars:
            stack = make_stack(stack, current_char)
            continue

        # making output
        if current_char in available_output_chars:
            output, stack = make_output(output, stack, current_char)
            continue

        if current_char == 'p':
            y = stack.pop()
            x = stack.pop()
            v = stack.pop()
            code[y][x] = str(v)
            continue
    return output
