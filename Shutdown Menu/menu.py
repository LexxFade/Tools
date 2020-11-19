#!/usr/bin/env python

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os

class mainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="SHUTDOWN MENU BLYAT")
		self.set_default_size(240, 100)
		self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        
		global headBox
		headBox = Gtk.Box()
		self.buttonLayout('/home/zulo/.config/i3/icons/shutdown.png', self.shutDown)
		self.buttonLayout('/home/zulo/.config/i3/icons/restart.png', self.reStart)
		self.buttonLayout('/home/zulo/.config/i3/icons/suspend.png', self.suspend)
		self.buttonLayout('/home/zulo/.config/i3/icons/Hibernate.png', self.hibernate)
		self.add(headBox)

	def buttonLayout(self, icon, command):
		button = Gtk.Button.new()
		image_icon = Gtk.Image.new_from_file(icon)
		button.set_image(image_icon)
		button.connect("clicked", command)
		headBox.add(button)
        
	def shutDown(self, button):
		os.system('shutdown -h now')
    
	def reStart(self, button):
		os.system('reboot')

	def hibernate(self, button):
		os.system('systemctl hibernate')

	def suspend(self, button):
		os.system('i3exit suspend')
		Gtk.main_quit()
		

win = mainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
