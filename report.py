#!/usr/bin/env python3.7

import fileinput
import sys
from datetime import datetime as dt

try:
  if '-h' in sys.argv[1]:
      sys.stderr.write(f'usage: {sys.argv[0]} <db name>\n')
      exit(1)
except IndexError:
    pass

events = []
buf = []
subsequent = False

for line in fileinput.input():
    ts, lift, count, weight = line.strip().split('|')
    if subsequent and count == '1':
        events.append(buf)
        buf = []
    buf.append((ts, lift, count, weight))

    subsequent = True

events.append(buf)

print('start lift count duration rpm weight')
for e in events:
    start_time, _, _, _= e[0]
    finish_time, lift, count, weight = e[-1]
    duration = dt.fromisoformat(finish_time) - dt.fromisoformat(start_time)
    try:
        print(
            start_time,
            lift,
            count,
            duration,
            int(int(count)/duration.seconds*60),
            weight,
        )
    except ZeroDivisionError:
        sys.stderr.write(f"bad record at {start_time}\n")
