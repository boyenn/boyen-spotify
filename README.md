# boyen-spotify

A simple global hotkey (CTRL+ALT+R) to save the currently playing song to a playlist. Very useful if you browse radios etc and don't want to swap to spotify all the time. I recommend using this together with https://github.com/attilagyongyosi/spotify-autohotkey (application to skip spotify songs etc with global hotkeys)

#Installation guide :

1. Download the exe from here : http://www.filedropper.com/boyen-spotify_4
2. Put it anywhere on your system
3. Create a new file called config.ini in the same directory as your boyen-spotify.exe (Make sure it's ANSI)
4. If you don't have one, create a lastfm account
5. Connect spotify with lastfm in your spotify desktop application's settings 
4. Refer to the next chapter for the config file content. Do this before going to the next step.
5. Start the exe
6. Press ctrl+alt+r (this is a global hotkey , should work anywhere on your system including games)
7. (This happens only one time, is for verification) You'll be prompted to copy paste an url into your browser. Do this and you'll get redirected to another url (starting with http://example.com)
8. Copy the url you were directed to back into program
9. From now on everytime you press ctrl+alt+R you'll save the currently playing song to your playlist

#Content of the config.ini file:

```
[lastfm]
user = user

[spotify]
userid : userid
playlistid : playlistid
```
Replace the fields user,userid,playlistid with the correct values
##User
Your lastfm username
##Userid and playlistid

Your user id and the id of the playlist that you want to add your music to.

To find these values , go to your spotify desktop application, rightclick your playlist and click "Copy Spotify-URL"

Paste this anywhere you want and you will get this format (this is mine for example) : spotify:user:119986897:playlist:129KfwIBp0N7pzlYlG7dOG

Now copy the values into the config






