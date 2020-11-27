#!/usr/bin/env ruby

kernel = `uname -r`
uptime = `uptime | sed 's/.*up \\([^,]*\\), .*/\\1/'`
packages = `pacman -Qq | wc -l`
icon_selected = rand(34)

icon_list = File.open("~/.scripts/art.txt", "r").readlines()
puts ""
puts ("  #{icon_list[(icon_selected * 6) + 1].chomp} OS..............: Arch Linux")
puts ("  #{icon_list[(icon_selected * 6) + 2].chomp} Kernel..........: #{kernel}")
puts ("  #{icon_list[(icon_selected * 6) + 3].chomp}")
puts ("  #{icon_list[(icon_selected * 6) + 4].chomp} Uptime..........: #{uptime}")
puts ("  #{icon_list[(icon_selected * 6) + 5].chomp} Packages........: #{packages}")
puts ""
