"""Generate some data"""

import random
import sys

LINES_COUNT = int(sys.argv[1])
FILENAME = f"data/data{LINES_COUNT}.txt"
MIN_ID = 9999
MAX_ID = 99999
MIN_VAL = 0
MAX_VAL = 1000
URL = "http://api.tech.com/item/"


with open(FILENAME, "w", encoding="utf-8") as fd:
    rand_pairs = (
        (random.randint(MIN_ID, MAX_ID), random.randint(MIN_VAL, MAX_VAL))
        for _ in range(LINES_COUNT)
    )
    output = "\n".join((f"{URL}{item_id} {value}" for item_id, value in rand_pairs))
    fd.write(output)
