#!/usr/bin/env bash

# add this script as an alias in shell-rc

fileName=$1
fileExe=${fileName::-3}".exe"

mcs $fileName
mono $fileExe
