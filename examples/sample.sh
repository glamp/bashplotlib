#!/usr/bin/env bash

dir=$(dirname "$0")

if [ ! -d "${dir}/data" ]; then 
    echo 'downloading data'
    "${dir}/downloaddata.sh"
fi

echo 'plotting coordinates'
scatter --file "${dir}/data/texas.txt"

echo 'with x and y coords'
scatter -x "${dir}/data/x_test.txt" -y "${dir}/data/y_test.txt"

echo 'plotting a histogram'
hist --file "${dir}/data/exp.txt"

echo 'with colors'
hist --file "${dir}/data/exp.txt" --colour blue

echo 'changing the shape of the point'
hist --file "${dir}/data/exp.txt" --pch .

echo 'adding x-labels'
hist --file "${dir}/data/exp.txt" --pch . --xlab

#echo 'using stdin'
#curl -sL https://dl.dropbox.com/u/49171662/example.txt | hist

#echo 'getting data from a webpage'
#curl -s 'http://www.baseball-reference.com' | 
#grep  -o -E '[$][0-9]+' | grep -o -E '[0-9]+' |
#hist -b 20 -t 'Baseball Payrolls' --height 20 --pch '*'
