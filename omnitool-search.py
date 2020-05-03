# these are some snippets that can be used for the search tool. they don't do much yet

import time
import shelve
from PIL import Image

screenshot_shelf_filename = r'.\screenshots.shelf'
reverse_index_filename = r'.\reverse_index.shelf'

database = shelve.open(screenshot_shelf_filename, flag='r')
db_keys = database.keys()
k = db_keys[8]
x = database[k]["text"]
print x
database.close()

reverse_index = shelve.open(reverse_index_filename, flag='r')
db_keys = reverse_index.keys()
print db_keys
reverse_index.close()
