#!/bin/zsh
echo "a- copy file to directory
b- copy multiple file to directory"
read op
if [[ "$op" = "a" ]]
then 
    echo "file name "
    read file 
    echo "directory name"
    read directory
    cp $file $directory
else
    echo "number of files "
    read n
    for i in $(seq 1 $n)
    do 
        echo "file name "
        read file 
        echo "directory name"
        read directory
        cp $file $directory
    done
fi

