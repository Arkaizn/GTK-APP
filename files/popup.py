#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, GLib, Gdk

class HyprlandHelperApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hyprland Helper")
        self.set_default_size(400, 300)
        
        # Load CSS before creating widgets
        self.load_css()
        
        # Main container
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)
        
        # Header - add CSS class
        header = Gtk.Label()
        header.set_markup("<big><b>Hyprland Helper</b></big>")
        header.get_style_context().add_class("header-label")
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
        
        # Status area - add CSS class
        self.status = Gtk.Label(label="Ready")
        self.status.get_style_context().add_class("status-label")
        box.pack_start(self.status, False, False, 10)
        
        # Quit button
        quit_btn = Gtk.Button(label="Quit")
        quit_btn.connect("clicked", Gtk.main_quit)
        box.pack_start(quit_btn, False, False, 10)
    
    def on_reload_clicked(self, button):
        self.status.set_text("Reloading Hyprland...")
        GLib.spawn_command_line_async("hyprctl reload")
        self.status.set_text("Hyprland reloaded!")
    
    def on_screenshot_clicked(self, button):
        self.status.set_text("Taking screenshot...")
        GLib.spawn_command_line_async("grim ~/screenshot-$(date +'%Y%m%d-%H%M%S').png")
        self.status.set_text("Screenshot saved in home directory!")
    
    def load_css(self):
        css = b"""
        window {
            background-color: #2d2d2d;
        }
        label {
            color: #ffffff;
        }
        button {
            background-color: #3c3c3c;
            color: #ffffff;
            border-radius: 5px;
        }
        button:hover {
            background-color: #4c4c4c;
        }
        .header-label {
            font-size: 18px;
            font-weight: bold;
        }
        .status-label {
            font-style: italic;
        }
        """
        
        # Try to load from file first, fall back to embedded CSS
        try:
            css_provider = Gtk.CssProvider()
            css_provider.load_from_path("style.css")
        except GLib.Error:
            css_provider = Gtk.CssProvider()
            css_provider.load_from_data(css)
        
        screen = Gdk.Screen.get_default()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen,
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

win = HyprlandHelperApp()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()