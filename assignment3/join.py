import MapReduce
import sys

"""
MapReduce for SQL like performance join
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order
    # value: line_item
    key = record[1]
    value = record
    
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: both ids
    # value: the whole record
    order = []
    line = []
    for v in list_of_values:
        if v[0] == "order":
            order.append(v)
        else:
            line.append(v)

    for o in order:
        for l in line:
            mr.emit(o + l)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
