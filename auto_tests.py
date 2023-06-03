import unittest
import Befunge_interpreter


class NamesTestCase(unittest.TestCase):

    def test_sieve_of_eratosthenes(self):
        result = Befunge_interpreter.interpret('2>:3g" "-!v\  g30          <\n'
                                               ' |!`"&":+1_:.:03p>03g+:"&"`|\n'
                                               ' @               ^  p3\\" ":<\n'
                                               '2 2345678901234567890123456789012345678')
        self.assertEqual('23571113171923293137', result)

    def test_hello_world(self):
        result = Befunge_interpreter.interpret('>25*"!dlroW olleH":v \n'
                                               '                v:,_@\n'
                                               '                >  ^   ')
        self.assertEqual('Hello World!\n', result)

    def test_factorial(self):
        result = Befunge_interpreter.interpret('08>:1-:v v *_$.@\n'
                                               '  ^    _$>\:^     ')
        self.assertEqual('40320', result)

    def test_quine(self):
        result = Befunge_interpreter.interpret('01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@')
        self.assertEqual('01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@', result)

    def test_addition(self):
        result = Befunge_interpreter.interpret('>34+.@')
        self.assertEqual('7', result)

    def test_subtraction(self):
        result = Befunge_interpreter.interpret('>43-.@')
        self.assertEqual('1', result)

    def test_multiplication(self):
        result = Befunge_interpreter.interpret('>43*.@')
        self.assertEqual('12', result)

    def test_integer_division(self):
        result = Befunge_interpreter.interpret('>82/.@')
        self.assertEqual('4', result)

    def test_integer_division_with_zero(self):
        result = Befunge_interpreter.interpret('>80/.@')
        self.assertEqual('0', result)

    def test_modulo(self):
        result = Befunge_interpreter.interpret('>92%.@')
        self.assertEqual('1', result)

    def test_modulo_with_zero(self):
        result = Befunge_interpreter.interpret('>82%.@')
        self.assertEqual('0', result)

    def test_logical_not(self):
        result = Befunge_interpreter.interpret('>5!.@')
        self.assertEqual('0', result)

    def test_logical_not_with_zero(self):
        result = Befunge_interpreter.interpret('>0!.@')
        self.assertEqual('1', result)

    def test_greater_than_bigger(self):
        result = Befunge_interpreter.interpret('>54`.@')
        self.assertEqual('1', result)

    def test_greater_than_smaller(self):
        result = Befunge_interpreter.interpret('>45`.@')
        self.assertEqual('0', result)

    def test_moving_right(self):
        result = Befunge_interpreter.interpret('>123...@')
        self.assertEqual('321', result)

    def test_moving_left(self):
        result = Befunge_interpreter.interpret('<@...123')
        self.assertEqual('123', result)

    def test_moving_down(self):
        result = Befunge_interpreter.interpret('>123v\n'
                                               '    .\n'
                                               '    .\n'
                                               '    .\n'
                                               '    @')
        self.assertEqual('321', result)

    def test_moving_up(self):
        result = Befunge_interpreter.interpret('v   @\n'
                                               '    .\n'
                                               '    .\n'
                                               '    .\n'
                                               '>123^')
        self.assertEqual('321', result)

    def test_moving_random_direction(self):
        result = Befunge_interpreter.interpret('>  v   \n'
                                               '@.1?2.@\n'
                                               '   3   \n'
                                               '   .   \n'
                                               '   @   ')
        self.assertIn(result, ['1', '2', '3'])  # kinda problematic

    def test_move_right_if_0(self):
        result = Befunge_interpreter.interpret('>  v   \n'
                                               '   0   \n'
                                               '@.1_2.@')
        self.assertEqual('2', result)

    def test_move_left_if_not_0(self):
        result = Befunge_interpreter.interpret('>  v   \n'
                                               '   3   \n'
                                               '@.1_2.@')
        self.assertEqual('1', result)

    def test_move_down_if_0(self):
        result = Befunge_interpreter.interpret('v  @ \n'
                                               '   . \n'
                                               '   1 \n'
                                               '>0 | \n'
                                               '   2 \n'
                                               '   . \n'
                                               '   @ ')
        self.assertEqual('2', result)

    def test_move_up_if_not_0(self):
        result = Befunge_interpreter.interpret('v  @ \n'
                                               '   . \n'
                                               '   1 \n'
                                               '>8 | \n'
                                               '   2 \n'
                                               '   . \n'
                                               '   @ ')
        self.assertEqual('1', result)

    def test_string_mode(self):
        result = Befunge_interpreter.interpret('>"olleH".....@')
        self.assertEqual('72101108108111', result)

    def test_duplicate_val_on_top_of_the_stack(self):
        result = Befunge_interpreter.interpret('>123:....@')
        self.assertEqual('3321', result)

    def test_duplicate_val_on_top_of_the_stack_empty_stack(self):
        result = Befunge_interpreter.interpret('>:.@')
        self.assertEqual('0', result)

    def test_swap_two_val_on_top_of_the_stack(self):
        result = Befunge_interpreter.interpret('>12\\..@')
        self.assertEqual('12', result)

    def test_swap_two_val_on_top_of_the_stack_one_val(self):
        result = Befunge_interpreter.interpret('>2\\..@')
        self.assertEqual('20', result)

    def test_pop_val_and_discard_it(self):
        result = Befunge_interpreter.interpret('>123$..@')
        self.assertEqual('21', result)

    def test_pop_val_and_output_as_integer(self):  # code wars requires string output, so it's correct
        result = Befunge_interpreter.interpret('>123...@')
        self.assertEqual('321', result)

    def test_pop_val_and_output_as_ASCII_char(self):
        result = Befunge_interpreter.interpret('>"olleH",,,,,@')
        self.assertEqual('Hello', result)

    def test_skip_next_cell(self):
        result = Befunge_interpreter.interpret('>12#3..@')
        self.assertEqual('21', result)

    # TODO: zaimplementuj obsługę znaków niestandardowych jak STX czy tabulacja pozioma
    def test_put_call(self):                  # 0123456789
        result = Befunge_interpreter.interpret('>250p ,@')  # zrób nowy test
        self.assertEqual('\x02', result)

    def test_get_call(self):                  # 0123456789
        result = Befunge_interpreter.interpret('>50g.9@')
        self.assertEqual('57', result)

    def test_end_program(self):                  # 0123456789
        result = Befunge_interpreter.interpret('>@')
        self.assertEqual('', result)

    def test_empty_spaces(self):                  # 0123456789
        result = Befunge_interpreter.interpret('>       @')
        self.assertEqual('', result)

    def test_codewars_test(self):
        result = Befunge_interpreter.interpret('>987v>.v\nv456<  :\n>321 ^ _@')
        self.assertEqual('123456789', result)


if __name__ == '__main__':
    unittest.main()
