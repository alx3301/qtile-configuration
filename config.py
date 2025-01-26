from libqtile import bar, layout
from libqtile.config import Screen

from hooks import *
from binds import *
from widgets import widgets

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
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [Screen(bottom=bar.Bar(size=30,widgets=widgets),
           wallpaper="/home/nameless/.config/qtile/resources/wallpaper.jpg")]
