"""
The class Language, which will be the base class for any defined language.
author:    Verstraeten Timothy
date:      04/14/2012
"""





class Language:
    """
    Defines a language by using bigrams.
    
    A language should be unique by name, not just by class name.
    When languages will be compared, they will be compared by name.
    """


    def __init__(self, name):
        self.table = {}
        self.name = name


    def get_name(self):
        return self.name


    def generate_table(self, page):
        """Generate the bigram-table using a given page. It keeps only track of alphabetic bigrams."""
        self.table = {}
        sum_prob = 0.0

        for i in range(len(page)-1):
            bigram = page[i:i+2].lower()
            if bigram[0].isalpha() and bigram[1].isalpha():
                if bigram not in self.table:
                    self.table[bigram] = 0
                self.table[bigram] += 1
                sum_prob += 1

        for i in self.table:
            self.table[i] /= sum_prob


    def shrink_table(self, size):
        """Shrink the table to the given size."""
        if size >= len(self.table):
            return
        else:
            sorted_table = sorted(self.table.items(), key=lambda x: x[1])
            sorted_table.reverse()
            self.table = {}

            sum_prob = sum([entry[1] for entry in sorted_table])
            for entry in sorted_table:
                self.table[entry[0]] = entry[1] / sum_prob
                

    def calc_probability(self, s):
        """Calculate the probability that this language contains the given string."""
        return sum([self.table[s[i:i+2]] for i in range(len(s)-1) if s[i:i+2] in self.table])
