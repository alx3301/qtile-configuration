flameshot &
telegram-desktop -startintray > /dev/null 2>&1 &
picom --config /home/nameless/.config/qtile/picom.conf &
setxkbmap -layout "us,ru" -option "grp:alt_shift_toggle" &
rclone mount Proton:/ ~/ProtonDrive --vfs-cache-mode writes &
