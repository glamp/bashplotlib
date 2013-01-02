#!/bin/bash


calc_axis_ticks() {
    local y_min=$1
    local y_max=$2
    local tickCount=$3

    local range=`echo "$y_max-$y_min" | bc`

    local unroundedTickSize=`echo "$range/($tickCount-1)" | bc`
    local x=`echo "l($unroundedTickSize)/l(10)-1" | bc -l`
    local pow10x=`echo "10^$x" | bc -l`
    local roundedTickRange=`echo "($unroundedTickSize / $pow10x) * $pow10x" | bc -l`
    echo "$roundedTickRange"
}


fname=$1
shape=${2:-o}

nums=`cat $fname`

ncount=`cat $fname | sort -n | uniq -c`
n_records=`cat $fname | wc -l`
n_bins=`echo "l($n_records)/l(2)+1" | bc -l`
#n_bins=`echo "sqrt($n_records)" | bc -l`
n_bins=${n_bins/.*}

if [[ $n_bins -gt 40 ]]; then
    n_bins=40
fi

min_val=`sort -n $fname | head -n 1`
max_val=`sort -n $fname | tail -n 1`

bin_size=`echo "scale=2; ($max_val-$min_val)/$n_bins" | bc` 

echo "records: $n_records"
echo "# of bins: $n_bins"
echo "bin size: $bin_size"
echo "min value: $min_val"
echo "max value: $max_val"
 
bars=();
 
lines_done=0
for n in $(seq $min_val $bin_size $max_val)
    do
        lines=`sort -n $fname | tail -n+$lines_done`
        n_lower=`echo "$n - $bin_size" | bc`
        size=`cat $fname | awk -v nl=$n_lower -v nu=$n '{ print (($1 < nu) == ($1 > nl)) ? "true" : "false"}' | grep "true" | wc -l`
        size=`echo "scale=2; 1000*($size/$n_records)" | bc`
        size=`echo "scale=0; $size/1" | bc`
        bars=("${bars[@]}" $size)
        lines_done=$((lines_done+$size))
    done
 
min_y=`echo ${bars[@]} | awk -v RS=" " '1'| sort -nr | tail -n 2`
max_y=`echo ${bars[@]} | awk -v RS=" " '1'| sort -nr | head -n 1`


echo
echo "  Bashplot"
echo

 
x_max=`echo "$n_bins*3" | bc`
x_axis_inc=`calc_axis_ticks $min_val $x_max 50`
y_axis_inc=`calc_axis_ticks 0 $max_y 25`

show_y_scale="YES"
for y in $(seq $max_y -$y_axis_inc $min_y)
    do
        if [[ "$show_y_scale" = "NO" ]]; then
            show_y_scale="YES"    
            y_line=`printf '%5s |' " "`
        else
            show_y_scale="NO"
            y_line=`printf '%5s |' $y`
        fi

        for bar in ${bars[@]}
            do
                if [[ $bar -ge $y ]]; then
                    y_line="$y_line $shape"
                else
                    y_line="$y_line  "
                fi
            done
        n_valid=`grep -o "$shape" <<<"$y_line" | wc -l`
        if [[ $n_valid -ne $n_bins ]]; then
            echo "$y_line"
            x=1
        fi
    done
 

printf "       " 
x_axis=`seq -s "-" $x_max | sed 's/[0-9]//g'`
echo $x_axis
printf "     "
x_labs=`seq -s "   " $min_val $x_axis_inc $x_max | sed -e 's/\.[0-9]*//g' -e 's/ *$//'`
x_len=${#x_axis}
#echo $x_labs
#echo $x_len
printf "%3s " ${x_labs:0:$x_len}
echo

