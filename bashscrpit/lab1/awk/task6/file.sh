#!/bin/zsh
cat /etc/passwd  |awk '{sub(/lp/,"mylp")}'| grep lp

