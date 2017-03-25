#!/bin/bash
function mysum(){
    local sum=$[$1+$2]
    echo $sum
}
a=1
b=2
mysum $a $b
echo $sum
