import peak.util.assembler

def gen_code(c, s_expr):
    """Generate code.
    """
    if isinstance(s_expr, list):
        gen_expression(c, s_expr)
    elif isinstance(s_expr, str):
        gen_variable(c, s_expr)
    elif isinstance(s_expr, (int, float)):
        gen_constant(c, s_expr)
    else:
        raise TypeError('Not a valid expression for code generation.')

def gen_expression(c, s_expr):
    """Generate code for S-expression.
    """
    name = s_expr[0]
    if name=='set!':
        gen_set(c, s_expr)
    elif name=='define':
        gen_set(c, s_expr)
    else:
        gen_function(c, s_expr)

def gen_set(c, s_expr):
    """Generate code for set!.

    The syntax for set! is (set! ident expr)
      Verify that the length of the S expression is 3.
      Verify that the second element is the name of the variable.
    """
    if len(s_expr) != 3:
        raise SyntaxError('Invalid set! expression.')
    gen_code(c, s_expr[2])
    c.STORE_NAME(s_expr[1])

def gen_function(c, s_expr):
    """Generate code for function call.

    The syntax for a functions call is (name expr1, expr2,... exprN).
    """
    gen_variable(c, s_expr[0])
    nargs = len(s_expr) - 1
    for e in s_expr[1:]:
        gen_code(c, e)
    c.CALL_FUNCTION(nargs)

def gen_variable(c, name):
    """Generate code for an identifier.

    LOAD_NAME by name.
    """
    c.LOAD_NAME(name)

def gen_constant(c, val):
    """Generate code for a literal.
 
    LOAD_CONST of value val.
    """
    c.LOAD_CONST(val)


if __name__=='__main__':
    import unittest
    from array import array
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
            self.assertEqual(self.c.co_code, array('B', [101, 0, 0, 131, 0, 0]))
            self.assertEqual(self.c.co_names, ['foo'])
        def test_gen_function_arg(self):
            """Verify generation of code for a function call
            with one argument.
            """
            s_expr = ['foo', 'x']
            gen_function(self.c, s_expr)
            self.assertEqual(self.c.co_code, array('B', [101, 0, 0, 101, 1, 0, 131, 1, 0]))
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
                   array('B', [101, 0, 0, 100, 1, 0, 101, 0, 0, 100, 2, 0, 100, 3, 0, 131, 2, 0, 131, 2, 0]))
            self.assertEqual(self.c.co_consts, [None, 2, 3, 4])
            self.assertEqual(self.c.co_names, ['add'])
    unittest.main()

