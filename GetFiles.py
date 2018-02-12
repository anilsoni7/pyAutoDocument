from os import chdir
from os import getcwd
from glob import glob

class GetFiles:
    def __init__(self,directory):
        self._directory = directory

    def get_file(self):
        chdir(self._directory)
        return getcwd(),glob("*.py")
