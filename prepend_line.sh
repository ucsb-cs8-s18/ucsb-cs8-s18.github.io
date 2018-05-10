#!/usr/bin/env bash


LINE=$1
FILE=$2
shift; shift;
# Having shifted twice, the rest is now comments ...
COMMENTS=$@
echo "Prepending $LINE to $FILE"
temp_file=$(mktemp)
echo $LINE >> $temp_file
cat $FILE >> $temp_file
cp $temp_file $FILE
/bin/rm $temp_file
