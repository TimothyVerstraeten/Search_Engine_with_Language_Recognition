"""
Dutch.
author:    Verstraeten Timothy
date:      04/14/2012
"""



from language import Language

class Dutch(Language):
    def __init__(self):
        Language.__init__(self, "Dutch")
        f = open("../res/dutch.txt")
        self.generate_table(f.read())
        f.close()
