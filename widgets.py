from libqtile.bar import STRETCH
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget import GroupBox, Prompt, WindowName, Systray, Clock, Spacer, CryptoTicker, HDD, Sep

sep = dict(padding=10, linewidth=1, size_percent=100)

widgets = [
    GroupBox(active="#20C20E",
             disable_drag=True,
             inactive="#0c4d06",
             highlight_method="line",
             this_current_screen_border="#20C20E",
             highlight_color=['#000000', '#000000']),

    Prompt(cursor=False,
           fmt="<b>{}</b>",
           record_history=False),

    WindowName(),

    Spacer(length=STRETCH),

    Clock(format="%Y-%m-%d %a %I:%M %p",
          decorations=[
              RectDecoration(
                  radius=5,
                  padding=0,
                  line_width=1,
                  line_colour="#20C20E")]),

    Systray(),

    Spacer(length=STRETCH),

    Sep(**sep),
    HDD(device="sda",
        format="[<b>HDD</b>: {HDDPercent:.0f}%]"),

    Sep(**sep),
    CryptoTicker(symbol="€",
                 crypto="XRP",
                 currency="EUR",
                 format="[<b>{crypto}</b>: {symbol}{amount:.2f}]"),
    Sep(**sep),
    CryptoTicker(symbol="€",
                 crypto="BTC",
                 currency="EUR",
                 format="[<b>{crypto}</b>: {symbol}{amount:.0f}]"),
    Sep(**sep),
    CryptoTicker(symbol="€",
                 crypto="TRUMP",
                 currency="EUR",
                 format="[<b>{crypto}</b>: {symbol}{amount:.0f}]"),
    Sep(**sep)]