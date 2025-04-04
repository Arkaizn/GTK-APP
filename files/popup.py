#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class HyprlandHelperApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hyprland Helper")
        self.set_default_size(400, 300)
        
        # Main container
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)
        
        # Header
        header = Gtk.Label()
        header.set_markup("<big><b>Hyprland Helper</b></big>")
        box.pack_start(header, False, False, 10)
        
        # Buttons
        buttons_box = Gtk.Box(spacing=5)
        box.pack_start(buttons_box, False, False, 0)
        
        # Reload Hyprland button
        reload_btn = Gtk.Button(label="Reload Hyprland")
        reload_btn.connect("clicked", self.on_reload_clicked)
        buttons_box.pack_start(reload_btn, True, True, 0)
        
        # Screenshot button
        screenshot_btn = Gtk.Button(label="Take Screenshot")
        screenshot_btn.connect("clicked", self.on_screenshot_clicked)
        buttons_box.pack_start(screenshot_btn, True, True, 0)
        
        # Status area
        self.status = Gtk.Label(label="Ready")
        box.pack_start(self.status, False, False, 10)
        
        # Quit button
        quit_btn = Gtk.Button(label="Quit")
        quit_btn.connect("clicked", Gtk.main_quit)
        box.pack_start(quit_btn, False, False, 10)
    
    def on_reload_clicked(self, button):
        self.status.set_text("Reloading Hyprland...")
        # Execute hyprctl reload in the background
        GLib.spawn_command_line_async("hyprctl reload")
        self.status.set_text("Hyprland reloaded!")
    
    def on_screenshot_clicked(self, button):
        self.status.set_text("Taking screenshot...")
        # Using grim for screenshot (common in Wayland)
        GLib.spawn_command_line_async("grim ~/screenshot-$(date +'%Y%m%d-%H%M%S').png")
        self.status.set_text("Screenshot saved in home directory!")

win = HyprlandHelperApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()