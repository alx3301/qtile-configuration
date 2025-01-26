from libqtile.lazy import lazy
from libqtile.config import Group, Key
from libqtile.utils import guess_terminal

mod = "mod4"

keys = [
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "w", lazy.window.kill()),
    Key([mod], "u", lazy.reload_config()),
    Key([mod], "o", lazy.spawn("chromium")),
    Key([mod], "p", lazy.spawn("virtualbox")),
    Key([mod],"f",lazy.window.toggle_fullscreen()),
    Key([mod], "t", lazy.window.toggle_floating()),
    Key([mod], "Return", lazy.spawn(guess_terminal())),
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