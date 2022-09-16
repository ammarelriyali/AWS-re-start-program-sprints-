#!/bin/zsh
cat /etc/passwd  | awk '{split($0,a,":"); print NR-1 " - " a[1],a[5],a[6]}'|head -n3
