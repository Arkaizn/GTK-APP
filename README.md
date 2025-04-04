# GTK App Launcher

![GTK](https://img.shields.io/badge/GTK-3.0-%234E9A06?logo=gtk)
![Python](https://img.shields.io/badge/Python-3.x-%233776AB?logo=python)
![License](https://img.shields.io/badge/License-MIT-blue)

A customizable GTK3 application launcher designed for seamless integration with Hyprland and other Wayland compositors.

## Features

- 🚀 Lightweight GTK3-based popup application
- 🎨 Customizable UI with CSS styling
- 🖥️ Optimized for Hyprland (floating windows, animations)
- ⚡ Fast Python implementation using PyGObject
- 🏗️ Modular design for easy extension

## Installation

### Prerequisites
- Python 3.x
- GTK 3.0 development libraries
- PyGObject

On Debian/Ubuntu:
``` sh
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0
```

On Arch Linux:
``` sh
sudo pacman -S python-gobject gtk3
```

### Clone and Run

``` sh
git clone https://github.com/arkaizn/GTK-APP.git
cd GTK-APP
python3 popup.py
```

### Hyprland Configuration
For optimal appearance, add these rules to your hyprland.conf


## License

This project is licensed under the MIT License - see the LICENSE file for details.
