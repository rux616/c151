#!/bin/bash

#Delete all the files in the directory specified by the first positional parameter (argument) that have the symbol ~ at the end.  These are backup files created by the editor emacs.  You can identify them with the expression $1/*~.
rm $1/*~
echo

#Delete all the files in the same directory that have the name core and any extension.
rm $1/core.*
echo

#Display a message saying that the emacs backup files and the core files have been deleted in that folder.
echo "emacs backup files and core files have been deleted in the folder '$1'"
echo

#Considering that this argument given to the script ($1) is a valid path, list the files that it contains.
ls $1
echo

#Display the number of positional parameters and all their values.
declare -i n ; n=$#+1
echo "There are are $n positional parameters."
echo "The first positional parameter (\$0) is $0."
echo "This is the command used to execute the script."
echo "The second positional paremeter (\$1) is $1."
echo "This is the argument used in the previous several commands to specify the directory where to run the various commands."
echo

#Display the content of the file .signature from your home directory (and not just from the current one) with the command cat, and outpuat a message before that explaining that this is your signature.
echo "This is my signature:"
cat ~djcassid/.signature
echo

#List the processes running from the terminal (not all running on the machine).
ps
