#!/bin/bash

rm -Rf ~/Documents/Image-Line/FL\ Studio/Settings/Hardware/Xtouch\ one*
rm -Rf ~/Documents/Image-Line/FL\ Studio/Settings/Hardware/xtouch_*
rm -Rf ~/Documents/Image-Line/FL\ Studio/Settings/Hardware/constants.py

cp -r ./dist/* ~/Documents/Image-Line/FL\ Studio/Settings/Hardware
