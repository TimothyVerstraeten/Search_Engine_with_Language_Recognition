"""
Portuguese.
author:    Verstraeten Timothy
date:      04/14/2012
"""



from language import Language

class Portuguese(Language):
    def __init__(self):
        Language.__init__(self, "Portuguese")
        f = open("../res/portuguese.txt")
        self.generate_table(f.read())
        f.close()
