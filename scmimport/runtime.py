"""runtime functions needed by scmimport implementation of the Scheme programming language.
"""

# Operators 
import operator

# Arithmetic operators
add = operator.add
sub = operator.sub
mul = operator.mul
div = operator.div

# Comparison operators
eq = operator.eq
ne = operator.ne
gt = operator.gt
lt = operator.lt
ge = operator.ge
le = operator.le

# functions for list processing
def car(x):
    return x[0]
def cdr(x):
    return x[1:]

