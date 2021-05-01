if [[ $# -eq 0 ]]; then
    echo "usage: $0 <duration>"
    exit 1
fi
rec -q -r48000 -traw - trim 0 $1
