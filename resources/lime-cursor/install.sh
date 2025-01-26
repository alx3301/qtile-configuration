#!/bin/bash
mkdir -p ~/.icons
cp -r lime-cursor ~/.icons/
if ! grep -q "export XCURSOR_THEME=lime-cursor" ~/.xinitrc; then
    echo "export XCURSOR_THEME=lime-cursor" >> ~/.xinitrc
fi
echo "The cursor has been installed. Restart your X session to apply the changes."
