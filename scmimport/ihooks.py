"""import hook for importing Scheme .scm source files."""
import sys      # need to add imported module to sys.modules
import os.path
import imp      # used to create module object

from . import compile


class ScmFinder(object):
    """Find .scm file on the Python path.

    If the .scm file was found an ScmLoader object is returned;
    otherwise, None is returned.

    Note: Currently, only the current working directory is checked
          for the file.
          TODO: Search the Python path for the file.
    """
    def find_module(self, fullname, path=None):
        filename = fullname + '.scm'
        if not os.path.exists(filename):
            return None
        else:
            return ScmLoader(filename)


class ScmLoader(object):
    """Load Python module for the .scm file.

    Note: Currently, an empty module object is created.
          TODO: Python bytecode gen.
    """
    def __init__(self, filename):
        self.filename = filename

    def load_module(self, fullname):
        """Create the module.

        During load, a number of steps are performed.
        1. A module object is created.
        2. The __file__ attribute is populated with the locations of
           the .scm file.
        3. The module is added to sys.modules.
        """
        mod_obj = imp.new_module(fullname)
        mod_obj.__file__ = self.filename
        sys.modules[fullname] = mod_obj
        # read the file and compile
        f = open(self.filename)
        c = compile.scmcompile(f.read(), self.filename)
        f.close()
        # Use eval to evalute the code object with the locals workspace
        #   provided by the module object's dict.
        eval(c, globals(), mod_obj.__dict__)
        return mod_obj
