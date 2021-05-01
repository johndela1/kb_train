duration=$1
lift=$2
if [ $# -ne 2 ]; then
  echo "usage: $0 <duration> <lift name>"
  exit 1
fi
for n in `seq 3 1`; do
  echo $n
  sleep 1
done
echo begin
./read_sound.sh $duration | ./count.py $lift | tee -a db.txt
play -n  synth 1 sin 300 2>/dev/null
