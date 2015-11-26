class worldlist(object):
    def __init__(self):
        self.direction = ['north','south',
                'east','west','down','up',
                'left','right','back']
        self.verbs = ['go','stop','kill','eat']
        self.stop_word=['the','in','of','from','at','it']
        self.nouns = ['door','bear','princess','cabinet']

    def convert_number(self,s):
        try:
            return int(s)
        except ValueError:
            return False

    def getsentense(self):
        self.sentense = raw_input('>')


    def scan(self,raw_inp):
        inp_split = raw_inp.split()
        out = []
        for inp in inp_split:
            if inp in self.direction:
                out.append(('direction',inp))
            elif inp in self.verbs:
                out.append(('verb',inp))
            elif inp in self.stop_word:
                out.append(('stop',inp))
            elif inp in self.nouns:
                out.append(('noun',inp))
            elif self.convert_number(inp):
                out.append(('number',self.convert_number(inp)))
            else:
                out.append(('error',inp))
        return out
        
