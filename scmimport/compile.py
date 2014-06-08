"""Compile Scheme code into a code object.
"""
import peak.util.assembler
from scm_parser import tokenize, parse
def scm_compile(source):
    """Compile source into code object.

    Compile the source into a code object. Code objects can be executed by a call to eval().
    """
    # parse the code into a parse tree.
    parse_tree = parse(tokenize(source))
    # generate code from the tree
    c = peak.util.assembler.Code()
    # TODO...

    # return the code object.
    return c.code()

