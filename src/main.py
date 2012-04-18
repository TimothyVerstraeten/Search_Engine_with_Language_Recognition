"""
Main function - Tests the Search Engine with Language Recognition
author:    Verstraeten Timothy
date:      04/14/2012
"""




from Search_Engine.search_engine import *
from Search_Engine.cache import cache



def compare_results(l1, l2):
    """Function to test whether two strings or two (unordered) lists of strings are the same."""
    if isinstance(l1, list):
        return (len(l1) == len(l2)) and all([elem in l2 for elem in l1])
    else:
        return (l1 == l2)




# Test 1: (Multi-)Lookup with Language Recognition
index, graph = crawl_web('http://timosenginetest.com/index.html')
print "=== TEST 1 (Search) ===\n"

result = compare_results(search(index, "Peter"),                              ['http://timosenginetest.com/barack_obama.html',
                                                                               'http://timosenginetest.com/barack_obama_dutch.html',
                                                                               'http://timosenginetest.com/pizza.html',
                                                                               'http://timosenginetest.com/tour_eiffel.html',
                                                                               'http://timosenginetest.com/real_madrid.html',
                                                                               'http://timosenginetest.com/berlin_wall.html',
                                                                               'http://timosenginetest.com/porto.html'])
result = result and compare_results(search(index, "Peter likes"),             ['http://timosenginetest.com/pizza.html',
                                                                               'http://timosenginetest.com/porto.html'])
result = result and compare_results(search(index, "Barack Obama"),            ['http://timosenginetest.com/barack_obama.html',
                                                                               'http://timosenginetest.com/barack_obama_dutch.html'])
print "Search:           \t" + str(result)

result = compare_results(search(index, "Peter", English()),                   ['http://timosenginetest.com/barack_obama.html'])
result = result and compare_results(search(index, "Barack Obama", English()), ['http://timosenginetest.com/barack_obama.html'])
print "Search (English): \t" + str(result)

result = compare_results(search(index, "Peter", Dutch()),                     ['http://timosenginetest.com/barack_obama_dutch.html'])
print "Search (Dutch):   \t" + str(result)

result = compare_results(search(index, "Peter likes", French()),              None)
result = result and compare_results(search(index, "Peter likes", Italian()),  ['http://timosenginetest.com/pizza.html'])
print "Search (Italian): \t" + str(result) + '\n\n'




# Test 2: Languages of the different pages
languages = Languages()
print "=== TEST 2 (Languages) ===\n"

result =            compare_results(get_language(get_page('http://timosenginetest.com/index.html'), languages).get_name(),              'English')
result = result and compare_results(get_language(get_page('http://timosenginetest.com/barack_obama.html'), languages).get_name(),       'English')
print "English:         \t" + str(result)

result = compare_results(get_language(get_page('http://timosenginetest.com/barack_obama_dutch.html'), languages).get_name(),            'Dutch')
result = result and compare_results(get_language(get_page('http://timosenginetest.com/manneken_pis.html'), languages).get_name(),       'Dutch')
print "Dutch:           \t" + str(result)

result = compare_results(get_language(get_page('http://timosenginetest.com/tour_eiffel.html'), languages).get_name(),                   'French')
print "French:          \t" + str(result)

result = compare_results(get_language(get_page('http://timosenginetest.com/berlin_wall.html'), languages).get_name(),                   'German')
print "German:          \t" + str(result)

result = compare_results(get_language(get_page('http://timosenginetest.com/pizza.html'), languages).get_name(),                         'Italian')
print "Italian:         \t" + str(result)

result = compare_results(get_language(get_page('http://timosenginetest.com/porto.html'), languages).get_name(),                         'Portuguese')
print "Portuguese:      \t" + str(result)

result = compare_results(get_language(get_page('http://timosenginetest.com/real_madrid.html'), languages).get_name(),                   'Spanish')
print "Spanish:         \t" + str(result)
