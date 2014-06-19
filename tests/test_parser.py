"""Test the simple Scheme parser."""
import unittest
from scmimport.parser import tokenize, parse


class TestTokenizer(unittest.TestCase):
    """Tokenizer tests."""
    def test_empty_expression(self):
        code = '()'
        tokens = tokenize(code)
        self.assertEqual(tokens, ['(', ')'])

    def test_set_expression(self):
        code = '(+ x y)'
        tokens = tokenize(code)
        self.assertEqual(tokens, ['(', '+', 'x', 'y', ')'])

    def test_expression_with_constant(self):
        code = '(set! x 23)'
        tokens = tokenize(code)
        self.assertEqual(tokens,
                        ['(', 'set!', 'x', '23', ')'])


class TestParser(unittest.TestCase):
    """Parser tests."""
    def test_basics(self):
        code = """
        (set! x 3)
        (+ x 2)
        (if y p q)
        (define a (if (= 2 3) (* 3 3) (* 4 4)))
        """
        tokens = tokenize(code)
        actT = []
        while tokens:
            actT.append(parse(tokens))
        expT = [['set!', 'x', 3],
                ['+', 'x', 2],
                ['if', 'y', 'p', 'q'],
                ['define', 'a', 
                    ['if',
                        ['=', 2, 3],
                        ['*', 3, 3],
                        ['*', 4, 4]]]]
        self.assertEqual(expT, actT)

    def test_empty_expresion(self):
        expExp = []
        actExp = parse(['(', ')'])
        self.assertEqual(len(actExp), len(expExp))

    def test_expression_with_int(self):
        expr = ['(', 'set!', 'x', '23', ')']
        expExp = ['set!', 'x', 23]
        actExp = parse(expr)
        self.assertEqual(actExp, expExp)

    def test_expression_with_float(self):
        expr = ['(', 'set!', 'x', '23.', ')']
        expExp = ['set!', 'x', 23.]
        actExp = parse(expr)
        self.assertEqual(actExp, expExp)


if __name__=='__main__':
    unittest.main()
