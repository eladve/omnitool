# THE QUERY (no user interface yet):
query_word = u"python"

# PLEASE EDIT THIS -- directories and file locations:
base_directory = r'C:\omnitool\\'
screenshot_shelf_filename = base_directory + r'screenshots.shelf'
inverted_index_filename = base_directory + r'inverted_index.shelf'
thumbnail_directory = base_directory + r'omnitool_thumbnails\\'

import time
import shelve
import editdistance
from PIL import Image
from omnitool_helper_functions import *

inverted_index = shelve.open(inverted_index_filename, flag='r')
inverted_index_keys = inverted_index.keys()
database = shelve.open(screenshot_shelf_filename, flag='r')
db_keys = database.keys()

try:
    search_word = canonicise_word(query_word)
    assert len(search_word)>=2
    if search_word not in inverted_index_keys:
        print "query not found"
    else:
        print len(inverted_index[search_word]), "screenshots found that countain the search term"
        last_hit = inverted_index[search_word][-1]
        assert last_hit in db_keys
        screenshot_filename = database[last_hit]["screenshot_file"]
        ocr_text = database[last_hit]["text"]
        display_screenshot_by_filename(screenshot_filename)
except:
    database.close()
    inverted_index.close()
    raise
