# the following program takes a screenshot every 10 seconds, OCRes it, and saves this to a shelf called screenshots. It also keeps another shelf containing a reverse dictionary pointing from every word that appeared in some screenshot, to the timestamps where that word has appeared. These two shelves can be used with a companion program to search for a word, producing all screenshots where that word has appeared.
# example intended usage: search for a word that you remember seeing on the screen. Get the screenshots where that word appeared. (Obviously this should be used to search for combinations of words, etc)
# Note: this code was written in a couple hours, so it's very preliminary. Might be a good base to start building on.

import time
import shelve
import pyautogui
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

screenshot_shelf_filename = r'.\screenshots.shelf'
reverse_index_filename = r'.\reverse_index.shelf'

def canonicise_word(w):
    try:
        w = str(w)
        w = w.strip("?-><:!@#$%^&*()""\\''.,~][{}]")
        if len(w) <= 1:
            return ""
        else:
            return w
    except UnicodeEncodeError:
        return ""    
        
database = shelve.open(screenshot_shelf_filename)
reverse_index = shelve.open(reverse_index_filename)


while True:
    t = int(time.time())
    t_key = str(t)
    screenshot = pyautogui.screenshot()
    screenshot_text = pytesseract.image_to_string(screenshot)
    database[t_key] = {"text" : screenshot_text, "screenshot" : screenshot}
    database.sync()
    # possible improvement: if the word bucket in two consecutive screenshots is similar, then for every word that repeats, replace the previous reverse index entry with the new one 
    words_in_screenshot = screenshot_text.split()  # TODO: remove parenthesis and other punctuation from words, maybe using split or strip or such. and remove words that come out empty. or single-letter words
    words_in_screenshot = [canonicise_word(w) for w in words_in_screenshot]
    for w in set(words_in_screenshot):
        if w not in reverse_index:
            reverse_index[w] = []
        list_w = reverse_index[w]
        reverse_index[w] = list_w + [t_key]
    reverse_index.sync()
    time.sleep(10)
