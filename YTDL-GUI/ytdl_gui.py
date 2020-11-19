#!/usr/bin/env python
import os
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Handler:
    def __init__(self):
        self.toExecute = ['youtube-dl -i -f ', "251", [], None]
        self.download_index = 1
        self.geoBypass = False
        self.operations = []
        self.countryCode = builder.get_object("entry_country_code")
        self.userEmail = builder.get_object("entry_username")
        self.userPass = builder.get_object("entry_password")
        self.passVisibility = False
        self.notification = builder.get_object("label_notification")
        try:
            os.system("mkdir /home/$USER/Videos/YouTube -p")
        except:
            pass
        self.window = builder.get_object("mainWindow")
        self.window
        self.window.show_all()

    def onDestroy(self, *args):
        Gtk.main_quit()
    
    def on_visible_toggled(self, widget):
        if self.passVisibility:
            self.passVisibility = False
        else:
            self.passVisibility = True
        self.userPass.set_visibility(self.passVisibility)

    def save_userinfo(self):
        try:
            self.userEmail_string = self.userEmail.get_text().strip()
            self.userPass_string = self.userPass.get_text().strip()   
            if (len(self.userPass) > 8 and len(self.userEmail) > 10):
                self.operations.append(f" -u {self.userEmail} -p {self.userPass} ")
            else:
                pass
        except:
            pass

    def random_location(self, widget):
        self.operations.append(" --geo-bypass")
        self.geoBypass = True

    def radio_option1(self, widget): #webm high audio
        self.toExecute[1] = "251"

    def radio_option2(self, widget): #m4a high audio
        self.toExecute[1] = "140"

    def radio_option3(self, widget): #webm audio (med)
        self.toExecute[1] = "250"

    def radio_option4(self, widget): #webm audio
        self.toExecute[1] = "249"

    def radio_option5(self, widget): #1080p
        self.toExecute[1] = "137"

    def radio_option6(self, widget): #720p
        self.toExecute[1] = "136"

    def radio_option7(self, widget): #480p
        self.toExecute[1] = "135"

    def radio_option8(self, widget): #360p
        self.toExecute[1] = "134"

    def radio_option9(self, widget): #240p
        self.toExecute[1] = "133"

    def radio_option10(self, widget): #144p
        self.toExecute[1] = "160"
    
    def country_code_info(self, widget):
        self.countryCode.set_text(" Go to https://www.countrycode.org/ for codes")

    def path_set(self):
        if len(user_path:=builder.get_object("entry_path").get_text().strip()) > 1:
            self.path = user_path + "/%(title)s-%(id)s.%(ext)s"
        else:
            self.path = r"/home/$USER/videos/%(title)s-%(id)s.%(ext)s "
        self.operations.append(f" -o {self.path}")
    
    def string_operations(self):
        try:
            if self.geoBypass:
                pass
            else:
                self.countryCode_text = self.countryCode.get_text().strip()
                if len(self.countryCode_text) > 0 and len(self.countryCode_text) < 5:
                    self.operations.append(f" --geo-bypass-country {self.countryCode_text} ")
        except:
            pass
        self.path_set()
        self.save_userinfo()
        self.toExecute[2] = ''.join(self.operations)

    def final_funtion(self, widget):
        self.string_operations()
        self.searchBar = builder.get_object("entry_url")
        self.toExecute[3] = self.searchBar.get_text().strip()
        try:
            self.toExecute_string = ''.join(self.toExecute)
            os.system(self.toExecute_string)
            self.notification.set_text(f"downloading {self.download_index} requests")
            self.operations = []
            self.download_index += 1
        except:
            pass

builder = Gtk.Builder()
builder.add_from_file("./Layout.xml")
builder.connect_signals(Handler())

Gtk.main()
