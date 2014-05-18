#!/usr/bin/env bash

if [ ! -d data ]; then
    mkdir data
fi
cd data

curl -L 'https://dl.dropbox.com/sh/jjeubxlxuqkzkeq/5W6zkUZXww/million.txt?dl=1' > million.txt
curl -L 'https://dl.dropbox.com/s/yuxlaj8okcjta9t/exp.txt?dl=1' > exp.txt
curl -L 'https://dl.dropbox.com/s/cbf5skx34grlwy6/lower48.txt?dl=1' > lower48.txt
curl -L 'https://dl.dropbox.com/s/gsu2y9vqnx5ps5i/texas.txt?dl=1' > texas.txt
curl -L 'https://dl.dropbox.com/s/4zws1nbamorcy9z/x_test.txt?dl=1' > x_test.txt
curl -L 'https://dl.dropbox.com/s/mlt4gfqr6n24kxj/y_test.txt?dl=1' > y_test.txt
