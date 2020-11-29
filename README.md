# Tools

### [CLI] 1 Line Scripts (Run C++, Run C & YTDL)
These scripts allows interaction with their associated program with just one command.
Should be added as an alias in shell config file, eg: `.bashrc` or `.zshrc`


### [CLI] AUR helper
A python script that uses webscraping to download (and install) packages from the [AUR](https://aur.archlinux.org/).


### [GUI] Shutdown Menu
A clean minimalistic power-menu written in Python using Gtk3 lib for i3wm. Certain lines can be edited to make it compatible for other DE/WM.
```py
38. def logout(self, button):
39.   os.system('i3-msg exit') # by changing this line
40.   Gtk.main_quit()
```
![shutdown menu](https://raw.githubusercontent.com/LexxFade/Tools/main/Shutdown%20Menu/screenshot.png)

### [CLI] Spotify Grabber
A script to download public playlists from spotify without using any API. <br>
*\*youtube-dl must be installed*


### [GUI] Scripte Animator
A tool to see what a sprite image would look like when converted into gif with different frame-rate.
framerate can be manually changed


### [CLI] System Info
Cleaner [neofetch](https://github.com/dylanaraps/neofetch) alternative with custom random icons everytime runned.
![System Info](https://raw.githubusercontent.com/LexxFade/Tools/main/System%20Info/terminal.png)

### [GUI] Youtube-dl GUI
GUI for [youtube-dl](),  a command line tool. <br>
Written in python using Gtk3 lib
![home](https://raw.githubusercontent.com/LexxFade/Tools/main/YTDL-GUI/home.png)
![advance](https://raw.githubusercontent.com/LexxFade/Tools/main/YTDL-GUI/advance.png)
