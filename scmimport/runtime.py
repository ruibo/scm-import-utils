"""runtime functions needed by scmimport
implementation of the Scheme programming language.
"""
import operator

# Arithmetic operators
add = operator.add
sub = operator.sub
mul = operator.mul
div = operator.div
pow = operator.pow

# Comparison operators
eq = operator.eq
ne = operator.ne
gt = operator.gt
lt = operator.lt
ge = operator.ge
le = operator.le


# basic forms
def iffunc(test, conseq, alt):
    return conseq if test else alt


# functions for list processing
def car(x):
    return x[0]


def cdr(x):
    return x[1:]


# A dictionary of the runtime functions.
__runtime__ = {
               '+': 'scmimport.runtime.add',
               '-': 'scmimport.runtime.sub',
               '*': 'scmimport.runtime.mul',
               '/': 'scmimport.runtime.div',
               '=': 'scmimport.runtime.eq',
               '>': 'scmimport.runtime.gt',
               '<': 'scmimport.runtime.lt',
               '>=': 'scmimport.runtime.ge',
               '<=': 'scmimport.runtime.le',
               'if': 'scmimport.runtime.iffunc',
               'car': 'scmimport.runtime.car',
               'cdr': 'scmimport.runtime.cdr'
              }
