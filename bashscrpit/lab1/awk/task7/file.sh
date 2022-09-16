#!/bin/zsh
cat /etc/passwd  | awk '{split($0,a,":");  }' |awk 'BEGIN{a=   0}{if ($3>0+a) a=$3} END{print a}'