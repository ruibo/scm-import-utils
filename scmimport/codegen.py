import peak.util.assembler
from . import runtime
runtime = runtime.__runtime__


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
    if name == 'set!':
        gen_set(c, s_expr)
    elif name == 'define':
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
    # check if the function is a run-time function.
    name = runtime.get(s_expr[0], s_expr[0])
    gen_variable(c, name)
    nargs = len(s_expr) - 1
    for e in s_expr[1:]:
        gen_code(c, e)
    c.CALL_FUNCTION(nargs)


def gen_variable(c, name):
    """Generate code for an identifier.

    LOAD_NAME by name.
    """
    if '.' in name:
        parts = name.split('.')
        c.LOAD_NAME(parts[0])
        for attr in parts[1:]:
            c.LOAD_ATTR(attr)
    else:
        c.LOAD_NAME(name)


def gen_constant(c, val):
    """Generate code for a literal.

    LOAD_CONST of value val.
    """
    c.LOAD_CONST(val)
