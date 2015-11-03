import MapReduce
import sys

"""
asymm friendships
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key  : person & friend (2 keys)
    # value: pair
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key,   (key, value))
    mr.emit_intermediate(value, (value, key))

def reducer(key, list_of_values):
    cleaned = set(list_of_values)
    for pair in cleaned:
        if list_of_values.count(pair) > 1:
            continue
        mr.emit(tuple(pair))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
