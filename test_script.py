import sys
import argparse

#days = sys.argv[1]
#print days

print "-" * 10

# Create parseer for input data
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--days')
    return parser

parser = createParser()
daystokeep = parser.parse_args(sys.argv[1:])

print daystokeep.days

