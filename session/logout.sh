#!/bin/bash

# options to be displyed
option0=" Logout"
option1=" Lock"
option2="⏾ Suspend"
option3="鈴 Hibernate"
option4=" Hybrid-sleep"
option5=" Reboot"
option6="襤 Shutdown"

# Variable passed to rofi
options="$option0\n$option1\n$option2\n$option3\n$option4\n$option5\n$option6"

selected="$(echo -e "$options" | rofi -theme-str  "inputbar{ children: [prompt];} listview{ lines: 7;}"  -dmenu -p "WARNING: unsaved changes will be lost")"
case $selected in
    $option0)
        # loginctl kill-session $(loginctl list-sessions | grep $USER);;
        sudo loginctl terminate-user $USER;;
    $option1)
        i3lock -c 000000;;
    $option2)
        sudo loginctl suspend;;
    $option3)
        systemctl hibernate;;
    $option4)
        systemctl hybrid-sleep;;
    $option5)
        sudo reboot;;
        # loginctl reboot;;
    $option6)
        sudo shutdown now;;
        # loginctl poweroff;;
esac
# This script is a fork of
# https://github.com/ItzSelenux/slnxwm/blob/main/scripts/logout
