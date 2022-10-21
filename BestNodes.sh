#!/bin/bash
for i in {1..9}
do
ssh Compute-00$i echo "Hello from node $i" >> BestNodesTest.txt
done
