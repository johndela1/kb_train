#!/usr/bin/env python3

import math
import subprocess
import sys
import time
from datetime import datetime as dt, timedelta


LC_RPM = 6
DURATION_MIN = 5

lifts = dict(
    lc=LC_RPM,
    snatch=LC_RPM * 2,
    jerk=LC_RPM * 1.5,
)


def tone(hz):
    subprocess.Popen(
        ["play", "-n", "synth", ".5", "sin", str(hz)],
        stderr=subprocess.DEVNULL,
    )


def parse(argv):
    try:
        lift = argv[1]
    except IndexError:
        sys.stderr.write(
            f"usage: {sys.argv[0]} <lift [{' '.join(lifts)}]>\n"
        )
        exit(1)

    if lift not in lifts:
        sys.stderr.write(f"lift not in {list(lifts.keys())}\n")
        exit(2)

    return lift


def round_up_to_even(x):
    return math.ceil(x / 2) * 2


def main(argv):
    lift = parse(argv)
    duration = timedelta(minutes=DURATION_MIN)
    rpm = lifts[lift]
    t1 = dt.now()
    period_sec = 60 / rpm
    count = round_up_to_even(rpm * duration.total_seconds() / 60)
    for i in range(count):
        if i == count - 1:
            hz = 400
        elif i == count / 2 - 1:
            hz = 400
        else:
            hz = 300
        tone(hz)
        time.sleep(period_sec)

    header = "ts lift count duration_m rpm"
    print(header)
    print(
        " ".join(
            (
                t1.isoformat().split(".")[0],
                lift,
                str(count),
                str(int((dt.now() - t1).total_seconds() / 60)),
                str(rpm),
            )
        )
    )


if __name__ == "__main__":
    main(sys.argv)
