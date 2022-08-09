#!/bin/bash

file="./data/badverbs_from_core_with_query.txt"
lines=$(cat $file)

for line in $lines
do
	wget $line
done

