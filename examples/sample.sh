#plotting coordinates
scatter -f ../data/texas.txt

#with x and y coords
scatter -x ../data/x_test.txt -y ../data/y_test.txt

#plotting a histogram
hist -f ../data/exp.txt

#with colors
hist -f ../data/exp.txt -c blue

#changing the shape of the point
hist -f ../data/exp.txt -p .

#using stdin
curl https://dl.dropbox.com/u/49171662/example.txt | hist

#getting data from a webpage
curl http://www.baseball-reference.com/ \
| grep  -o -E "[$]([0-9]+)" | grep -o -E "[0-9]+" \
| hist -b 20 -t "Baseball Payrolls" --height 20 --pch "*"


