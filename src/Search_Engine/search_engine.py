"""
Search Engine with Language Recognition.
author:    Udacity CS101; Verstraeten Timothy
date:      04/14/2012
version:   2.0
"""





import re
from Languages.languages import *
from cache import cache



def search(index, keywords, language = None):
    """Looks up a string or a query of words in order in the given index. By giving an optional argument, which should be a well-defined language, only the urls of the pages in that language will be returned."""
    if not(isinstance(keywords, list)):
        keywords = keywords.split()

    result = lookup(index, keywords[0], language)
    for i in range(1, len(keywords)):
        for entry in result:
            entry[1] += 1
        nextLookup = lookup(index, keywords[i], language)
        result = [entry for entry in nextLookup if entry in result]
        if not(result):
            return None
    return [entry[0] for entry in result]



def crawl_web(seed):
    """Crawl the web with the given seed page."""
    languages = Languages()
    tocrawl = [seed]
    crawled = []
    graph = {}
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            language = get_language(content, languages)
            add_page_to_index(index, page, content, language)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph



def get_page(url):
    """Search the cache for the page corresponding to the url. Returns None if the url isn't found."""
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        return None



def get_next_target(page):
    """Get the first url in the given page."""
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote



def get_all_links(page):
    """Get all links in the given page."""
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links



def union(a, b):
    """Returns the union of two lists."""
    for e in b:
        if e not in a:
            a.append(e)



def add_page_to_index(index, url, content, language):
    """Adds an url and language at the given keys in the content of a page, in the given index."""
    words = content.split()
    for i in range(len(words)):
        add_to_index(index, words[i], i, url, language)



def add_to_index(index, keyword, pos, url, language):
    """Adds an url and language at the given key in the index."""
    if keyword in index:
        index[keyword].append([url, language, pos])
    else:
        index[keyword] = [[url, language, pos]]



def lookup(index, keyword, language = None):
    """Lookup a keyword in the given index. By giving an optional argument, which should be a well-defined language, only the urls of the pages in that language will be returned."""
    if keyword in index:
        result = [entry for entry in index[keyword] if not(language) or entry[1].get_name() == language.get_name()]
        return [[entry[0], entry[2]] for entry in result]
    else:
        return []



def get_language(page, languages):
    """Get the language of the given page. The language will be chosen from the given languages."""

    #Removing the tags from a page will increase the chance of finding the right language.
    page = remove_tags(page)
    values = [(language.calc_probability(page), language) for language in languages]
    return max(values)[1]



def remove_tags(page):
    """Remove the tags (anything between '<' and '>') from a page."""
    pattern = re.compile(r'<.*>')
    return pattern.sub('', page)
