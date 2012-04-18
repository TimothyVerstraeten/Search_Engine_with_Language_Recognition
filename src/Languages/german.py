"""
German.
author:    Verstraeten Timothy
date:      04/14/2012
"""



from language import Language

class German(Language):
    def __init__(self):
        Language.__init__(self, "German")
        f = open("../res/german.txt")
        self.generate_table(f.read())
        f.close()
