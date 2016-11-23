#!/usr/bin/env python

import cgi
import json
import time
import tntfl.constants as Constants
from tntfl.ladder import TableFootballLadder
import tntfl.transforms.transforms as PresetTransforms

form = cgi.FieldStorage()


def add(record, time, cur):
    record[int(time)] = cur

ladder = TableFootballLadder(Constants.ladderFilePath, transforms=PresetTransforms.transforms_for_ladder())
times = form.getfirst('at')
activePlayers = {}
if times is not None:
    [add(activePlayers, time, ladder.getNumActivePlayers(int(time))) for time in times.split(',')]
else:
    add(activePlayers, time.time(), ladder.getNumActivePlayers())

print 'Content-Type: application/json'
print
print json.dumps(activePlayers)
