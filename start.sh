#!/bin/bash

directories=("change_header" "forum_php" "sandbox" "sqli" "sqli_blind" "ssti")

for dir in "${directories[@]}"
do
    echo "Starting in directory: $dir"
    (cd "$dir" && ./start.sh)
done

echo "All scripts have been started."