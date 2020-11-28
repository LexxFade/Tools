#!/usr/bin/env bash

kernel=`uname -r`
uptime=`uptime | sed 's/.*up \([^,]*\\), .*/\1/'`
packages=`pacman -Q| wc -l`
selected=$(( RANDOM % 34 * 6 ))

index=0
while IFS= read -r line
do
  if [ $index -eq $(( selected + 1 )) ]; then
    echo "  $line OS..............: Arch Linux"
	elif [ $index -eq $(( selected + 2 )) ]; then
    echo "  $line WM..............: i3wm + gaps"
	elif [ $index -eq $(( selected + 3 )) ]; then
    echo "  $line Kernel..........: $kernel"
	elif [ $index -eq $(( selected + 4 )) ]; then
    echo "  $line Uptime..........: $uptime"
	elif [ $index -eq $(( selected + 5 )) ]; then
    echo "  $line Packages........: $packages"
  fi
  ((index = index + 1))
done < art.txt
