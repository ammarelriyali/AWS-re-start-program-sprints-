#!/bin/zsh 
cat /etc/passwd  |awk 'NR>=5&&NR<=15' 