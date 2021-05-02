duration=$1
lift=$2

if [ $# -ne 2 ]; then
  echo "usage: $0 <duration> <lift name>"
  exit 1
fi

sleep 2
play -n  synth 1 sin 300 2>/dev/null
./read_sound.sh $duration | ./count.py $lift | tee -a $db && \
play -n  synth 1 sin 300 2>/dev/null
