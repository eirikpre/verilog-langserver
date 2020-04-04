
class Database:

    def __init__(self):
        # Defined macros and defines
        self._macros = {}
        # Declared objects
        self._files = {}


    @property
    def declarations(self):
        declarations = {}
        for f in self._files:
            for o in f.declarations:
                declarations.update(o)
        return declarations

    @property
    def macros(self):
        pass


class File:
    def __init__(self, filename):
        self.filename = filename
        self.objects = {}

class Declaration:
    def __init__(self):
        self.name = None
        self.type = None
        self.file = None
        self.start = None
        self.end = None


class Macro(Declaration):
    pass


class Position:
    def __init__(self, line, char):
        self.line = line
        self.char = char
