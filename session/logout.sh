#!/bin/bash

# options to be displyed
option0=" Logout"
option1="⏾ Suspend"
option2="鈴 Hibernate"
option3=" Hybrid-sleep"
option4=" Reboot"
option5="襤 Shutdown"

# Variable passed to rofi
options="$option0\n$option1\n$option2\n$option3\n$option4\n$option5"

selected="$(echo -e "$options" | rofi -theme-str  "inputbar{ children: [prompt];} listview{ lines: 6;}"  -dmenu -p "WARNING: unsaved changes will be lost")"
case $selected in
    $option0)
        # loginctl kill-session $(loginctl list-sessions | grep $USER);;
        loginctl terminate-user $USER;;
    $option1)
        loginctl suspend;;
    $option2)
        systemctl hibernate;;
    $option3)
        systemctl hybrid-sleep;;
    $option4)
        reboot;;
        # loginctl reboot;;
    $option5)
        shutdown now;;
        # loginctl poweroff;;
esac
# This script is a fork of
# https://github.com/ItzSelenux/slnxwm/blob/main/scripts/logout