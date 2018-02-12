
class ReadFile:
    def _init__(self):
        pass

    def read_file(self,filename=None):
        if filename is None:
            return
        l = list()
        with open(filename,'r') as f:
            for line in f:
                l.append(line)

        f.close()
        return l
