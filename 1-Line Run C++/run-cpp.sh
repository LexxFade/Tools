#!/bin/env bash

# compile and execute c++ scripts in one command
# have this as an alias in your shell rc

rm new_script

g++ -o new_script $1

./new_script
