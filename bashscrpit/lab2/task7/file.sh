#!/bin/bash
type=""
if [[ -f $1 ]]
then 
    echo "it is file "
    type="file"
else 
    echo "it is directory "
    type="directory"
fi
if [ -r $1 ]
then 
    echo $type" has read permission"
elif [ -w $1 ]
then 
    echo $type" has write permission"
else

    echo $type" has execute permission"
fi