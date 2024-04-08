#!/bin/bash

directories=("change_header" "forum_php" "sqli" "sqli_blind" "ssti" "prototype_pollution" "xss" "file_upload" "file_download")

for dir in "${directories[@]}"; do
    echo "Starting in directory: $dir"
    (cd "$dir" && ./start.sh)
done

echo "All dockers have been started."
