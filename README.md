# Qtile config
![Screenshot](.screenshot.png)

## Requirements: 
> Note: The following packages have the name they appear under in Arch Linux.
If you use another distribution, find the equivalent packages

### Qtile:
```
python-dbus-next python-psutil python-pywlroots python-setproctitle python-xdg xorg-xwayland
```

### Config:
Configurable:
- `sakura` (terminal)
- `gsimplecal` (calendar)
- `pavucontrol` (soundctl)

Used in the autostart:
- `mate-polkit` (for pkexec)
- `gnome-keyring` (for store passwords)
- `network-manager-applet` (for manage networks connections via nm-applet)
- `volctl` (for volume control)
- `lxqt-powermanagement` (for power management)
- `rofi` (for launch programs and logout)
- `nerd-fonts` (for icons in logout)

## Recomends: 
- `notify-osd` (to recive notifications)
- `lxappearance` (to manage gtk theme and icons)
- `kvantum` (to manage qt theme)
- `qt5ct` (to manage qt icons and set the kvantum theme)

## Setup
```bash
cd ~/.config/
git clone https://github.com/Anonyzard/qtile
```