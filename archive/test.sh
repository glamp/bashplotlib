#!/bin/bash

xy=`paste -d "," data/*_test.txt`
xy=`paste -d "." data/*_test.txt | sort -n`

n=`sed -n '$=' data/x_test.txt`

seq -s "-" 21 | sed 's/[0-9]//g'


points=();
for x in $(seq -11 1 11)
    do
        blank=`seq -s ".-" 1 21 | sed 's/[0-9]//g'`
        points=("${points[@]}" $blank)
   done


for plt_y in $(seq -11 1 11)
    do
    for plt_x in $(seq -11 1 11)
        do
        for line in $xy
            do

                point=$(echo $line | tr "." "\n")
                x=${point[0]}
                y=${point[1]}
                
#                echo $plt_y, $plt_x
#                echo $y, $x                
                if [[ $y -eq $plt_y ]]; then
                    printf "x"
                elif [[ $plt_y -eq 0 ]]; then
                    printf "-"
                elif [[ $plt_x -eq 0 ]]; then
                    printf "|"
                else
                    printf " "
                fi

            done
        done
        printf "\n"
    done

echo DONE
#for y in $(seq -11 1 11)
#    do
#        for x in $(seq -11 1 11)
#            do
#                if [[ $y -eq 0 ]]; then
#                    printf "-"
#                elif [[ $x -eq 0 ]]; then
#                    printf "|"
#                elif [[ 2 -eq 4 ]]; then
#                    printf "x"
#                else
#                    printf " "
#                fi
#            done
#
#        printf "\n"
#
#    done

