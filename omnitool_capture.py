# the following program takes a screenshot every 10 seconds, OCRes it, and saves this to a shelf called screenshots. It also keeps another shelf containing an inverted index pointing from every word that appeared in some screenshot, to the timestamps where that word has appeared. These two shelves can be used with a companion program to search for a word, producing all screenshots where that word has appeared.
# example intended usage: search for a word that you remember seeing on the screen. Get the screenshots where that word appeared. (Obviously this should be useful to search for combinations of words, etc)
# Note: this code was written in a couple hours, so it's very preliminary. Might be a good base to start building on.

# PLEASE EDIT THIS -- directories and file locations:
base_directory = r'C:\omnitool\\'
screenshot_shelf_filename = base_directory + r'screenshots.shelf'
inverted_index_filename = base_directory + r'inverted_index.shelf'
thumbnail_directory = base_directory + r'omnitool_thumbnails\\'

import time
import os
import shelve
import pyautogui
import pytesseract
from PIL import Image
from omnitool_helper_functions import *
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# START:

if not os.path.isdir(base_directory):
    os.mkdir(base_directory)
if not os.path.isdir(thumbnail_directory):
    os.mkdir(thumbnail_directory)
database = shelve.open(screenshot_shelf_filename)
inverted_index = shelve.open(inverted_index_filename)

print "running omnitool capture. (This runs infinitely. to stop this, kill the program.)"

try:
    while True:
        t = int(time.time())
        t_key = str(t)

        # take screenshot and OCR it:
        screenshot = pyautogui.screenshot()
        screenshot_text = pytesseract.image_to_string(screenshot)

        # reduce screenshot size and store it:
        compressed_screenshot_filename = thumbnail_directory + t_key + ".jpeg" 
        compress_screenshot_and_save(screenshot, compressed_screenshot_filename)
        database[t_key] = {"text" : screenshot_text, "screenshot_file" : compressed_screenshot_filename}
        database.sync()
        
        # update inverted index: (actually doesn't have to do this right now; can always create the index from the database file at any time)
        words_in_screenshot = screenshot_text.split()
        words_in_screenshot = [canonicise_word(w) for w in words_in_screenshot]
        for w in set(words_in_screenshot):
            if w not in inverted_index:
                inverted_index[w] = []
            list_w = inverted_index[w]
            inverted_index[w] = list_w + [t_key]
        inverted_index.sync()
        
        # rinse, repeat
        time.sleep(10)
except:
    database.close()
    inverted_index.close()
