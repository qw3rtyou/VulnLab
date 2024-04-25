a=`echo */`
echo $a

for dir in $a; do
    echo "Starting in directory: $dir"
    (cd "$dir" && docker-compose down)
done