#!/bin/bash

directories=`echo */`

for dir in "${directories[@]}"; do
    echo "Starting in directory: $dir"
    (cd "$dir" && ./start.sh)
done

echo "All dockers have been started."
