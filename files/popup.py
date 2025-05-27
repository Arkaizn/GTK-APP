#!/usr/bin/env python3
import os
import sys

# Ensure style.css is found regardless of how the script is launched
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, GLib, Gdk
from gi.repository.Gdk import KEY_Escape

class HyprlandHelperApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hyprland Helper")
        # Close on Escape
        self.connect("key-press-event", self.on_key_press)
        self.set_default_size(400, 300)

        # Load any custom overrides (only if style.css exists)
        self.load_css()

        # Main container
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        # Header label
        header = Gtk.Label()
        header.set_markup("<big><b>Hyprland Helper</b></big>")
        header.get_style_context().add_class("header-label")
        box.pack_start(header, False, False, 10)

        # Buttons container
        buttons_box = Gtk.Box(spacing=5)
        box.pack_start(buttons_box, False, False, 0)

        # Reload button
        reload_btn = Gtk.Button(label="Reload Hyprland")
        reload_btn.connect("clicked", self.on_reload_clicked)
        buttons_box.pack_start(reload_btn, True, True, 0)

        # Screenshot button
        screenshot_btn = Gtk.Button(label="Take Screenshot")
        screenshot_btn.connect("clicked", self.on_screenshot_clicked)
        buttons_box.pack_start(screenshot_btn, True, True, 0)

        # Status label
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

    def on_key_press(self, widget, event):
        if event.keyval == KEY_Escape:
            Gtk.main_quit()

    def load_css(self):
        css_path = os.path.join(script_dir, 'style.css')
        if not os.path.exists(css_path):
            return
        provider = Gtk.CssProvider()
        provider.load_from_path(css_path)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

if __name__ == '__main__':
    win = HyprlandHelperApp()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()