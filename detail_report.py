#!/usr/bin/env python3.7

import fileinput
import sys
from datetime import datetime as dt

try:
    if "-h" in sys.argv[1]:
        sys.stderr.write(f"usage: {sys.argv[0]} <db name>\n")
        exit(1)
except IndexError:
    pass
header = "ts lift count duration rpm weight"
print(header)


def calc(start, end):
    start_time, _, _, _ = start
    end_time, lift, count, weight = end
    duration = dt.fromisoformat(end_time) - dt.fromisoformat(start_time)
    try:
        return (
            start_time,
            lift,
            count,
            duration,
            int(int(count) / duration.seconds * 60),
            weight,
        )
    except ZeroDivisionError:
        sys.stderr.write(f"bad record at {start_time}\n")


def pr(items):
    print(" ".join(str(i) for i in items))


for iter_count, line in enumerate(fileinput.input()):
    rec = tuple(line.strip().split("|"))
    count = int(rec[2])
    if count == 1:
        if iter_count:
            pr(calc(start_rec, prev_rec))
        start_rec = rec
    prev_rec = rec
pr(calc(start_rec, prev_rec))
