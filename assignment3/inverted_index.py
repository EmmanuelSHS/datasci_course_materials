#!/usr/bin/env python
# coding=utf-8
#import re
#import json
import MapReduce
import sys

"""
inverted_index in MapReduce
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # text/key
    # id/value
    value = record[0]
    print value
    keys = record[1]
    keys = keys.split()
    for k in keys:
      mr.emit_intermediate(k, value)
#    pattern = re.compile(r"[\w']+")
#    for line in record:
#        lline = json.loads(line)
#        # split para into words
#        id = lline[0]
#        words = re.findall(pattern, lline[1])
#        for text in words:
#            mr.emit_intermediate(text, id)
#
def reducer(key, list_of_values):
    # key: word
    # value: the document id
    total = []
    for v in list_of_values:
      # + in list get one with all char elements, append get str elements
      if v not in total:
        total.append(v)
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
