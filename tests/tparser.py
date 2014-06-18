"""Test the simple Scheme parser."""
import unittest
from scmimport.parser import tokenize, parse

class TParser(unittest.TestCase):
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
