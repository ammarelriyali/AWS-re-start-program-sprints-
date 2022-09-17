#!/bin/zsh
echo "–l: list in long format
–a: list all entries including the hiding files.
–d: if an argument is a directory, list only its name
–i: print inode number
–R: recursively list subdirectories

"
if [ -z $1 ]
then 
ls ~    
elif [ -z $2 ]
then 
ls $1
else
    case $1 in 
    -a)
     ls -a $2 
     ;;
    -l) 
    ls -l $2 
    ;;
    -d) 
    ls -d $2 
    ;;
    -i) 
    ls -i $2
    ;;
    -r) 
    ls -R $2 
    ;;
    *) echo "renter option again pls" 
    ;;
    esac
fi