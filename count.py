#!/usr/bin/env python3

import random
import struct
import sys
from datetime import datetime as dt

weight_kg = 12

lifts = (
    "swing",
    "lswing",
    "rswing",
    "longcycle",
    "llongcycle",
    "rlongcycle",
    "snatch",
    "lsnatch",
    "rsnatch",
    "jerk",
    "ljerk",
    "rjerk",
)

try:
    lift = sys.argv[1]
except IndexError:
    sys.stderr.write(f"usage: {sys.argv[0]} <lift name>\n")
    exit(1)
if lift not in lifts:
    sys.stderr.write(f"not in {lifts}\n")
    exit(2)


FORMAT = "<i"  # single 32 bit integer
SAMPLERATE = 48e3

count = 0

with open("/dev/stdin", "rb", buffering=0) as stdin:
    decay = 0
    while True:
        try:
            raw = stdin.read(struct.calcsize(FORMAT))
            v = struct.unpack(FORMAT, raw)[0]
        except struct.error:
            break
        if decay:
            decay -= 1
            continue
        if abs(v) > 12e6:
            count += 1
            decay = SAMPLERATE

            rec = "|".join(
                (
                    dt.now().isoformat().split(".")[0],
                    lift,
                    str(count),
                    str(weight_kg),
                )
            )
            print(rec, flush=True)
