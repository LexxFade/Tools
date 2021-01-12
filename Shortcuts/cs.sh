#!/usr/bin/env bash

fileName=$1
fileExe=${fileName::-3}".exe"

mcs $fileName
mono $fileExe
