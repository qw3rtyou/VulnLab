a=`echo */`
echo $a

for dir in $a; do
    echo "Starting in directory: $dir"
    (cd "$dir" && ./start.sh)
done