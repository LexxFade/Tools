#!/usr/bin/env sh

# wont have to remember format numbers :/

Link=$1
youtube-dl -F $Link
echo ""
echo "Enter format: "
read Format
youtube-dl -f $Format $Link
