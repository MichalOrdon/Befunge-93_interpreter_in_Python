import unittest
import Befunge_interpreter


class NamesTestCase(unittest.TestCase):

    def test_addition(self):
        result = Befunge_interpreter.interpret('>34+.@')
        self.assertEqual('7', result)

    def test_substraction(self):
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


'''

    def test_test(self):
        result = Befunge_interpreter.interpret('>.@')
        self.assertEqual('', result)
        
'''

if __name__ == '__main__':
    unittest.main()
