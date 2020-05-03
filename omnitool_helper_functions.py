from PIL import Image

def canonicise_word(w):
# this function takes a string representing a word and makes it more canonical, by stripping punctuation, etc
# TODO: to enable good search quality, need to make this better, e.g. by using maybe using some NLP library to kern the word, etc
# also, I think the whole program doesn't work propertly on non-latin text; maybe even not on non-english text.
    try:
        w = str(w).lower()
        w = w.strip("?-><:!@#$%^&*()""\\''.,`~][{}]")
        if len(w) <= 1:
            return ""
        else:
            return w
    except UnicodeEncodeError:
        return ""

def compress_screenshot_and_save(screenshot, filename):
    compressed_screenshot = screenshot.copy()
    compressed_screenshot.thumbnail((720,1280))
    compressed_screenshot.save(filename, format="JPEG", quality=0, optimize=True, qtables = "web_low", subsampling = 2) 
    return
