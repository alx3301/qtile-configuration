from libqtile import hook
from subprocess import Popen

@hook.subscribe.startup_once
def autostart():
    Popen(args="/home/nameless/.config/qtile/autostart.sh", shell=True)