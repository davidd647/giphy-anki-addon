# Add-on: Auto-fetch Relevant Gifs


Hey!

## Background: 
Wrote some JS and stuff a while back to take info from the {{Back}} of your card, and display a relevant gif from giphy.com. I thought I could make it better... So I did!

## Problems:
- It's not super-fun to memorize things, and that's a deal-breaker for lots of people.
- It might be fun if you had awesome and varied visuals while you studied, but that sounds like a lot of work.
- Problem with the last solution: Using JS, you had to download the gif every time you opened a card (slow!)

## Solution:
- Automatically take text from your answer field, get a relevant gif from GIPHY API, and add it to the back of your card!
- Solution for the problem from last time: I decided to use Python so the gif is downloaded onto your device only once! (well, maybe twice if you count syncing your data to your phone or w/e)

----

(Disclaimer: There may still be some bugs. This is more experimental than production-class code. If you bump into a bug, feel free to let me know!)

----

## How to Set Up:
1. Go to  https://github.com/davidd647/giphy-anki-addon
2. Go to https://developers.giphy.com/ and sign up for an API key
3. On the right, there's a green "Clone or download" button, clone or download.
4. Open Anki --> Tools --> Add-ons --> View Files
5. That will show you a folder. Each add-on has its own folder here. Add the files into a new folder
6. Go into the add-on folder and add a file called setup.py
7. In that file, write these two lines:
  ```
  apiKey = "YOUR_GIPHY_API_KEY"
  downloadPath = "FULL_PATH_TO_ANKI'S_MEDIA_FOLDER"
  ```
8. Replace YOUR_GIPHY_API_KEY with your API key from Giphy (did that at the beginning!)
9. Replace FULL_PATH_TO_ANKI'S_MEDIA_FOLDER with your full path to Anki's collection.media folder
10. Restart Anki


## How to Use:
1. Make sure there is a "Back" field and a "Giphy" field on your card
2. Type something into your card's "Back", and click somewhere else on the screen
3. Your "Giphy" field should be auto-filled with a relevant gif!

-----

Issues with my approach:
- If you're kinda playing around, it's kinda easy to end up with a bunch of unused gifs in your media folder. That said, you can always 
- There's lots of steps getting it set up, right? I hope I wrote that clearly enough...

-----

Bonus:
- There's a resultsLimit variable in __init__.py. It's set to 1 by default, but if you increase that number, you can get a whole bunch of gifs at the same time!