import unittest
import peak.util.assembler
from array import array
from scmimport.codegen import gen_constant
from scmimport.codegen import gen_variable
from scmimport.codegen import gen_function
from scmimport.codegen import gen_set 
from scmimport.codegen import gen_expression


class TestCodeGen(unittest.TestCase):
    """TestCodeGen test generation of Python bytecode.

    Test that the correct Python code object can be
    generated from Scheme S-expressions.
    """
    def setUp(self):
        """Construct a new code object for each test."""
        self.c = peak.util.assembler.Code()

    def test_gen_constant(self):
        """Verify generation of code for a constant."""
        gen_constant(self.c, 23)
        self.assertEqual(self.c.co_code, array('B', [100, 1, 0]))
        self.assertEqual(self.c.co_consts, [None, 23])

    def test_gen_variable(self):
        """Verify generation of code for an identifier."""
        gen_variable(self.c, 'x')
        self.assertEqual(self.c.co_code, array('B', [101, 0, 0]))
        self.assertEqual(self.c.co_names, ['x'])

    def test_gen_function_noargs(self):
        """Verify generatin of code for a function call
        with no arguments.
        """
        s_expr = ['foo']
        gen_function(self.c, s_expr)
        self.assertEqual(self.c.co_code,
                         array('B', [101, 0, 0, 131, 0, 0]))
        self.assertEqual(self.c.co_names, ['foo'])

    def test_gen_function_arg(self):
        """Verify generation of code for a function call
        with one argument.
        """
        s_expr = ['foo', 'x']
        gen_function(self.c, s_expr)
        self.assertEqual(self.c.co_code,
                         array('B', [101, 0, 0, 101, 1, 0, 131, 1, 0]))
        self.assertEqual(self.c.co_names, ['foo', 'x'])

    def test_gen_set(self):
        """Verify generation of code for assignment."""
        s_expr = ['set!', 'x', 12]
        gen_set(self.c, s_expr)
        self.assertEqual(self.c.co_code, array('B', [100, 1, 0, 90, 0, 0]))
        self.assertEqual(self.c.co_names, ['x'])
        self.assertEqual(self.c.co_consts, [None, 12])

    def test_gen_expression(self):
        """Verify generation of code for an S-expression."""
        s_expr = ['add', 2, ['add', 3, 4]]
        gen_expression(self.c, s_expr)
        self.assertEqual(self.c.co_code,
                         array('B',
                               [101, 0, 0,
                                100, 1, 0,
                                101, 0, 0,
                                100, 2, 0,
                                100, 3, 0,
                                131, 2, 0,
                                131, 2, 0]))
        self.assertEqual(self.c.co_consts, [None, 2, 3, 4])
        self.assertEqual(self.c.co_names, ['add'])


if __name__=='__main__':
    unittest.main()
