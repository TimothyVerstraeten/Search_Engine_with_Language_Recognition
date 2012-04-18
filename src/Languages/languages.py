"""
Languages which are available to the Search Engine. (extendable)
author:    Verstraeten Timothy
date:      04/14/2012
"""




from english import English
from dutch import Dutch
from french import French
from german import German
from italian import Italian
from portuguese import Portuguese
from spanish import Spanish



class Languages:
    """Contains the defined languages."""


    def __init__(self):
        #The list of languages can be extended.
        self.languages = [English(), Dutch(), French(), German(), Italian(), Portuguese(), Spanish()]

        #This size can be adjusted by giving an integer parameter to the function. Be aware that a size too low can lead to a poor evaluation of the languages,
        #and a size too high can be 'unfair' to languages who aren't big enough. (which will also lead to a poor evaluation.) 
        self.shrink_tables()


    def __getitem__(self, key):
        return self.languages[key]


    def shrink_tables(self, size=300):
        """Shrink the size of the languages (tables) to the given size."""
        for language in self.languages:
            language.shrink_table(size)
