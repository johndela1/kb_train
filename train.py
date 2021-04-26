#!/usr/bin/env python3

import random
import time
from datetime import datetime as dt

dur_sec = 60
weight_kg = 12

lifts = dict(
    swing=None,
    long_cycle=None,
    snatch=None,
)

for lift in lifts:
    print(f'begin {lift}')
    t1 = dt.now()
    elapsed = 0
    while elapsed < dur_sec:
        elapsed = (dt.now() - t1).seconds
        print(dur_sec - elapsed)
        time.sleep(1)
    lifts[lift] = input('input count: ')

with open('db.txt', 'a') as f:
    for k,v in lifts.items():
        rec = '|'.join((k, v, str(dur_sec), str(weight_kg)))+'\n'
        f.write(rec)
