import MapReduce
import sys

"""
Matrix Multi
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: dna trimed
    # value: 1
    l = len(record[1])
    key = record[1][:l - 10]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
