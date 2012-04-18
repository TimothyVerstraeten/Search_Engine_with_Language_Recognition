"""
Spanish.
author:    Verstraeten Timothy
date:      04/14/2012
"""



from language import Language

class Spanish(Language):
    def __init__(self):
        Language.__init__(self, "Spanish")
        f = open("../res/spanish.txt")
        self.generate_table(f.read())
        f.close()
