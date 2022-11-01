# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess
from libqtile import qtile
qsession = qtile.core.name

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

if qsession == "wayland":
    from libqtile.backend.wayland import InputConfig

    wl_input_rules = {
    # Use "qtile cmd-obj -o core -f get_inputs" to verify the identifier of your touchpad
    # https://docs.qtile.org/en/latest/manual/wayland.html#libqtile.backend.wayland.InputConfig
    "1267:12632:ELAN050A:00 04F3:3158 Touchpad": InputConfig(tap=True, # Tap to click
    tap_button_map="lrm", # 1/2/3 fingers, l=left, r=right, m=middle
    accel_profile="adaptive", # flat, adaptive, on_button_down, none
    dwt=False, # Disable touchpad while typing
    drag=True, # drag & drop
    scroll_method="two_finger", # two_finger, edge, on_button_down, none
    natural_scroll=False,
    middle_emulation=True, click_method="button_areas"),

    "*": InputConfig(left_handed=False, pointer_accel=True),
    "type:keyboard": InputConfig(kb_layout="latam", kb_variant="", kb_options=""),
    }

home = os.path.expanduser('~')
mod = "mod4"
terminal = guess_terminal() # set your terminal, guess_terminal() for default
calendar = "gsimplecal" # set your app for calendar
soundctl = "pavucontrol" # set your app mixer if you don´t use volctl
logout = lazy.spawn(home+"/.config/qtile/session/logout.sh") # a rofi script to logout

#Theme 
barBackground = "#1d2021"
primaryColor = "#eee0b7"
secondaryColor = "#111111"
wallpaper= home+"/.config/1041.png" # /path/to/image


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "c", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "space", lazy.spawn("rofi -show-icons -show drun"), desc="Launch rofi"),
    #Key(["mod1"], "Tab", lazy.spawn("notify-send 'Alt+Tab'")),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "i", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "i", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],"Return",lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"), #"Return"
    # Toggle between different layouts as defined below
    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "F4", logout, desc="Logout"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Sound
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ toogle")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +5%")), # systemd
    # Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")), #no-systemd 
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5-%")), #systemd
    # Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")), #no-systemd 
]

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus=primaryColor,border_normal=secondaryColor,border_width=4),#border_focus_stack=["#d75f5f", "#8f3d3d"]
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        # bottom=subprocess.run(["tint2"]), # Using tint2
        bottom=bar.Bar(
            [
                widget.CurrentLayoutIcon(background=barBackground,mouse_callbacks={"Button1": lazy.spawn("rofi -show-icons -show drun"), "Button3": lazy.next_layout()}),
                widget.GroupBox(highlight_method="block",background=barBackground),
                widget.Prompt(background=barBackground),
                widget.WindowName(background=barBackground),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),background=barBackground
                ),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f",background=barBackground),
                widget.CapsNumLockIndicator(fmt="|{}|",background=barBackground),
                widget.Net(format='↓ {down}\n↑ {up}',prefix="k",background=barBackground),# ↓ ↑ {interface}:
                # widget.Volume(fmt='|Vol: {}|',background=barBackground,volumeapp="pavucontrol",mouse_callbacks={"Button3": lazy.spawn(soundctl)}),
                widget.Systray(background=barBackground), # Only x11
                # widget.StatusNotifier(background=barBackground), # Use this for wayland
                widget.Battery(update_interval=30,fmt="{}",format='{char} {percent:2.0%} \n  {hour:d}:{min:02d}  ',
                background=barBackground, charge_char="↑", discharge_char="↓",low_percentage=0.3),
                widget.Clock(format="%H:%M:%S\n%a %d/%m/%Y",background=barBackground, mouse_callbacks={"Button3": lazy.spawn(calendar)}),
                # widget.QuickExit(background=barBackground,default_text='',fontsize=30, countdown_format='[{}\nseconds]'),
                widget.TextBox("",fontsize=30,background=barBackground,mouse_callbacks={"Button1": logout}),
            ],
            28,#34,#24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        wallpaper=wallpaper,
        wallpaper_mode="fill",
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag(["control"], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=primaryColor
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
# wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
@hook.subscribe.startup_once
def autostart():
    subprocess.Popen([home + '/.config/qtile/session/autostart.sh'])
