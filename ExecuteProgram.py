from subprocess import Popen
from os import chdir
from os import getcwd
from os import listdir
from os import system
import sys

class ExecuteProgram:
    def __init__(self):
        self._aim = ""

    def execute(self,path,filename=None):
        if filename is None :
            print("Please specify file name to execute")
            sys.exit(0)
        
        chdir(path)
        #print(getcwd())
        print("")
        self._filename = filename
        self._process = Popen(["cmd", "@cmd", "/k", "cls","&&", "python","-u",str(filename)])
        #print(self._process.communicate()[0])
        
        
    def wait(self):
        self._process.wait()

    def terminate(self):
        self._process.terminate()

    def set_aim(self,aim):
        self._aim = aim
        
    def get_aim(self):
        return self._aim
