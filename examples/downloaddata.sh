#!/usr/bin/env bash

dir=$(dirname "$0")

if [ ! -d "${dir}data" ]; then
    mkdir "${dir}/data"
fi

curl -L 'https://dl.dropbox.com/sh/jjeubxlxuqkzkeq/5W6zkUZXww/million.txt?dl=1' > "${dir}/data/million.txt"
curl -L 'https://dl.dropbox.com/s/yuxlaj8okcjta9t/exp.txt?dl=1' > "${dir}/data/exp.txt"
curl -L 'https://dl.dropbox.com/s/cbf5skx34grlwy6/lower48.txt?dl=1' > "${dir}/data/lower48.txt"
curl -L 'https://dl.dropbox.com/s/gsu2y9vqnx5ps5i/texas.txt?dl=1' > "${dir}/data/texas.txt"
curl -L 'https://dl.dropbox.com/s/4zws1nbamorcy9z/x_test.txt?dl=1' > "${dir}/data/x_test.txt"
curl -L 'https://dl.dropbox.com/s/mlt4gfqr6n24kxj/y_test.txt?dl=1' > "${dir}/data/y_test.txt"
