# Developed by d2dev_
# 2019-04-03
# License: Iunno - use this stuff however you want, if you'd like!



# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *
from anki.hooks import addHook

#######################
# Giphy setup

import json, re, urllib
import urllib.request
import os.path

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from .setup import *
resultsLimit = "1"
##########################


# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction():
  # get the number of cards in the current collection, which is stored in
  # the main window
  cardCount = mw.col.cardCount()
  # show a message box
  showInfo("Card count: %d" % cardCount)

# create a new menu item, "test"
action = QAction("test", mw)
# set it to call testFunction when it's clicked
action.triggered.connect(testFunction)
# and add it to the tools menu
mw.form.menuTools.addAction(action)


#####

def onFocusLost(flag, note, fidx):
  # flag: flag, n: note, fidx: current field
  src = None
  dst = None
  # showInfo("n: %s" % n)         # <anki.notes.Note object at 0x11a686eb8>
  # showInfo("fidx: %s" % fidx)   # 1
  # showInfo("flag: %s" % flag)   # false
  # has src and dst fields?

  # enumerate assigns an index to c, and a value to name
  for index, name in enumerate(mw.col.models.fieldNames(note.model())):
    # showInfo("c: %s" % c)       # 0, 1, 2... maybe it's the index
    # showInfo("name: %s" % name) # Front, Back Wiki
    if "Back" == name:
      src = "Back"
      srcIndex = index
    if "Giphy" == name:
      dst = "Giphy"
  if not src or not dst:
    return flag
  # event coming from src field?
  if fidx != srcIndex:
    return flag
  # grab source text
  srcTxt = mw.col.media.strip(note[src])
  if not srcTxt:
    return flag
  
  # update field
  # wikipedia.set_lang("en") # can also be fr, en, jp
  # query = wikipedia.summary(srcTxt, sentences=2)

  searchQuery = srcTxt

  # Construct the URL to use for Giphy's API
  giphyUrl = "http://api.giphy.com/v1/gifs/search?q=" + searchQuery + "&api_key=" + apiKey + "&limit=" + resultsLimit

  # Get info back from Giphy's API
  results = json.loads(urllib.request.urlopen(giphyUrl).read())['data']

  # Pattern to take unique codes from the gifs we get
  regex = r"(\/media\/(\w+)\/)\w+"

  giphyResultString = ""
  # For each gif
  for result in results:
    # Dive into the object (library? list?) and get a URL for the gif
    downloadUrl = result[u'images'][u'fixed_height_small'][u'url']
    
    # If there's a good name we can give the gif (the code in the URL)
    match = re.search(regex, downloadUrl)

    # Create the filename for the file
    filename = match.group(2) + ".gif"

    giphyResultString += f"<img src=\"{filename}\">"

    # Get the file, and save it as the filename
    resp = urllib.request.urlopen(downloadUrl)
    with open(os.path.join(downloadPath,filename), 'wb') as f:
      f.write(resp.read())
  
  note[dst] = giphyResultString

  return True

addHook('editFocusLost', onFocusLost)
