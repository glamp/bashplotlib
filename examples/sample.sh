echo plotting coordinates

scatter --file ./data/texas.txt

echo with x and y coords
scatter -x ./data/x_test.txt -y ./data/y_test.txt

echo plotting a histogram
hist --file ./data/exp.txt

echo with colors
hist --file ./data/exp.txt --colour blue

echo changing the shape of the point
hist --file ./data/exp.txt --pch .

echo using stdin
curl https://dl.dropbox.com/u/49171662/example.txt | hist

echo getting data from a webpage
curl http://www.baseball-reference.com/ \
| grep  -o -E "[$]([0-9]+)" | grep -o -E "[0-9]+" \
| hist -b 20 -t "Baseball Payrolls" --height 20 --pch "*"


