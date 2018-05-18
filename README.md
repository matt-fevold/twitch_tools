# Twitch-Tools

A simple program to display the current playing spotify song.

Motivation - I did not want to run a large application just to run the current playing song (snip) and I wanted a bit more control over how that's displayed.

### to run:

download requirements.

Run visualizer. Follow prompt.



### how it works:

It finds the window id for spotify (why you have to click on it, as finding the foreground window was dead simple)
 and prints off the name of that window (for spotify it conviniently is ```Song - Artist```) 
 
: )



# Magic Card Viewer
It is still in progress but it was inspired by MtgGoldfish's stream overlay for cards. It aims to crop
a magic card for just the top of it, add the name of the card onto the image. It will end up using
an api from https://scryfall.com/ to get the image data but that isn't implemented yet.
