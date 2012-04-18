"""
French.
author:    Verstraeten Timothy
date:      04/14/2012
"""



from language import Language

class French(Language):
    def __init__(self):
        Language.__init__(self, "French")
        f = open("../res/french.txt")
        self.generate_table(f.read())
        f.close()
