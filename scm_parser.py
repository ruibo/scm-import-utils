"""Parser Parses lisp expressions.

This code is based on Peter Norvig's lis.py implementation 
of a subset of Scheme in Python. 
"""
def tokenize(s):
    """Tokenize a string into Scheme tokens.

    Convert a string into a list of tokens.
    """
    return s.replace('(',' ( ').replace(')',' ) ').split()
def parse(tokens):
    """Parse a list of tokens into a Syntax tree.

    Convert a list of tokens into a tree.
    """
    if len(tokens)==0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token=='(':
        L = []
        while tokens[0] != ')':
            L.append(parse(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token==')':
        raise SyntaxError('unexpected )')
    else:
        return token

if __name__=='__main__':
    pass

