from libqtile import bar, layout
from libqtile.config import Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from hooks import *
from widgets import widgets

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod],"f",lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )

layouts = [
    layout.MonadTall(
        margin=15,
        border_width=1,
        border_focus="#20c20e",
        border_normal="#0c4d06"
    ),
]

widget_defaults = dict(
    font="terminus",
    foreground="#20c20e",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [Screen(bottom=bar.Bar(size=24,widgets=widgets),
           wallpaper="/home/nameless/.config/qtile/wallpaper.jpg")]