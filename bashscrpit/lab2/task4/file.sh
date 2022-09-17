#!/bin/zsh 
#run scrpit with . 
echo "pls run script with . before it "
if [ -z $1]
then 
cd ~
else 
cd $1
fi