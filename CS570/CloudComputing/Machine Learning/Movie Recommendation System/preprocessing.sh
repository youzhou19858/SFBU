#!/bin/bash  

while read -r line
do
  echo "$line" | tr [:space:] ',' > input
done < u.data