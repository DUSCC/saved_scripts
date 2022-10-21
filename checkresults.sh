#!/bin/bash

for i in {1..9}
do
echo "compute-00${i}: " ; sed '47,47!d' compute-00${i}_xhpl.txt
done

for i in {10..99}
do
echo "compute-0${i}: " ; sed '47,47!d' compute-0${i}_xhpl.txt
done

for i in {100..400}
do
echo "compute-${i}: " ; sed '47,47!d' compute-${i}_xhpl.txt
done
