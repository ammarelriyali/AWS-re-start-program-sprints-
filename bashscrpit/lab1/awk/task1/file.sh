#!/bin/zsh 
cat /etc/passwd  | awk '{split($0,a,":"); print a[1],a[5]}'
