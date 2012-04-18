"""
Italian.
author:    Verstraeten Timothy
date:      04/14/2012
"""



from language import Language

class Italian(Language):
    def __init__(self):
        Language.__init__(self, "Italian")
        f = open("../res/italian.txt")
        self.generate_table(f.read())
        f.close()
