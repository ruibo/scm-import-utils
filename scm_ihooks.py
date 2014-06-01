"""ihooks for importing .scm files.
"""
import sys
import os.path
import imp # used to create module object

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
        return mod_obj

# add to meta_path
sys.meta_path.append(ScmFinder())

