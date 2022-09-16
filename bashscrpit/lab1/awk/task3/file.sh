#!/bin/zsh
cat /etc/passwd  | awk '{split($0,a,":");  print a[1],a[3],a[5]}'|awk '$2>500 {print ;}'
