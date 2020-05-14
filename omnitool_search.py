# THE QUERY (no user interface yet):
query = u"marketplace supply demand twitter"
# put a single word, or a collection of words seperated by spaces (the algorithm will search a screenshot containing all of these words

# PLEASE EDIT THIS -- directories and file locations:
base_directory = r'C:\omnitool\\'
screenshot_shelf_filename = base_directory + r'screenshots.shelf'
inverted_index_filename = base_directory + r'inverted_index.shelf'
thumbnail_directory = base_directory + r'omnitool_thumbnails\\'

import time
import random
import shelve
import editdistance
from PIL import Image
from omnitool_helper_functions import *

inverted_index = shelve.open(inverted_index_filename, flag='r')
inverted_index_keys = inverted_index.keys()
database = shelve.open(screenshot_shelf_filename, flag='r')
db_keys = database.keys()

try:
    finished = False
    search_words = query.split()
    search_words = [canonicise_word(word) for word in search_words]
    search_words = [word for word in search_words if len(word)>=2]
    assert len(search_words)>=1
    for word in search_words:
        if word not in inverted_index_keys:
            print "search term -- ", word, " -- not found"
            finished = True
    if not finished:
        hits = [set(inverted_index[word]) for word in search_words]
        # hits is a list of sets. now compute the AND of all these sets:
        final_hits = hits[0]
        for h in hits[1:]:
            final_hits = final_hits & h
        final_hits = list(final_hits)
        random.shuffle(final_hits)
        if len(final_hits) == 0:
            print "no screenshots found that contain all the search terms"
        else:
            print len(final_hits), "screenshots found that countain the search terms"
            for hit in final_hits[:10]:
                assert hit in db_keys
                screenshot_filename = database[hit]["screenshot_file"]
                print hit, "   ", screenshot_filename, ":"
                display_screenshot_by_filename(screenshot_filename)
                print
except:
    database.close()
    inverted_index.close()
    raise
