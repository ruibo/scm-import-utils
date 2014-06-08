"""Compile Scheme source into a code object."""
import peak.util.assembler
from parser import tokenize, parse
from . import codegen

def scmcompile(source, filename):
    """Compile Scheme source into code object.

    Compile the source into a code object. Code objects can be executed by a call to eval().
    """
    # parse the code into a parse tree.
    parse_tree = parse(tokenize(source))

    # Do some initialization 
    # Note:
    #   Currently, peak.util.assembler is required by this file
    #   plus codegen.py. The dependence on the outside module
    #   should be abstracted away. In addition, the codegen.py
    #   file could probably be combined with this file.
    c = peak.util.assembler.Code()
    c.co_name = '<module>'
    c.co_firstlineno = 1
    c.co_filename = filename
    c.co_flags = 64 # Not sure why?

    # generate code from the tree
    codegen.gen_code(c, parse_tree)    

    # Hack for now, need to load and return None.
    c.LOAD_CONST(None)
    c.RETURN_VALUE()

    # emit the code object.
    return c.code()

