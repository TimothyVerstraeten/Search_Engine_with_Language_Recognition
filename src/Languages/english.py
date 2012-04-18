"""
English.
author:    Verstraeten Timothy
date:      04/14/2012
"""



from language import Language

class English(Language):
    def __init__(self):
        Language.__init__(self, "English")
        f = open("../res/english.txt")
        self.generate_table(f.read())
        f.close()
