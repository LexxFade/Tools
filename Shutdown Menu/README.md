### Shutdown Menu
Simple bloat-less powermenu for minimalitic i3wm.

### Libs used:
- Gtk
- OS

![shutdown menu](https://raw.githubusercontent.com/LexxFade/Tools/main/Shutdown%20Menu/screenshot.png)


### Use for other DE/WM
Edit these linesto make it compatible for other systems.
```py
38. def logout(self, button):
39.   os.system('i3-msg exit') # by changing this line
40.   Gtk.main_quit()
```
