import os
import glob

class GetFiles:
    def __init__(self, directory):
        self._directory = directory

    def get_file(self):
        os.chdir(self._directory)
        return os.getcwd(), glob.glob("*.py")
