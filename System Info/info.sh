#!/usr/bin/env bash
KERNEL=`uname -r`
UPTIME=`uptime | cut -c 2-9`
PACKAGES=`pacman -Qq | wc -l`

echo $''
echo $'  ░░╚══╗░╔═╔════╝    OS..............: Arch Linux'
echo $"  ╚═╦═╗╠═╩═╩╗╔═╦═╗   Kernel..........:" $KERNEL
echo $'  ░░║▒╠╣▒▒▒▒╠╣▒║▒║'
echo $"  ╔═╩═╝╠═╦═╦╝╚═╩═╝   Uptime..........:" $UPTIME
echo $"  ░░╔══╝░╚═╚════╗    Packages........:" $PACKAGES
echo $''
