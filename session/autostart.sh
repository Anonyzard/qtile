#!/bin/bash
# X11 Configs
if [ $XDG_SESSION_TYPE = x11 ];then
xinput set-prop 13 305 0
setxkbmap latam
fi

# rofi -dmenu -p "Bienvenido" -theme-str "listview{ lines: 0;}" &
dunst &
# Polkit
/usr/lib/mate-polkit/polkit-mate-authentication-agent-1 &

# gnome-keyring
/usr/bin/gnome-keyring-daemon --start --components=pkcs11 &
/usr/bin/gnome-keyring-daemon --start --components=secrets &
/usr/bin/gnome-keyring-daemon --start --components=ssh &

#picom --experimental-backends & # Picom with blur
#feh --bg-fill /usr/share/backgrounds/1586.jpg & # Wallpaper with feh
# /usr/lib/notification-daemon-1.0/notification-daemon -r &

lxqt-powermanagement &
nm-applet &
volctl &


#alttab
alttcolor="#eee0b7"
alttbg="#1d2021"
alttfg="#ffffff"
alttab -fg $alttfg -bg $alttbg -frame $alttcolor -inact $alttcolor -t 400x30 -i 64x64 -w 1  -vertical -bc $alttcolor -bw 3
