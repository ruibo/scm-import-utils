"""
scmimport provides support for importing
a Scheme .scm file as a Python module.
"""

# There are no exports in this module.
__all__ = ()

# add ihook to meta_path
import sys
from . import ihooks
sys.meta_path.append(ihooks.ScmFinder())
