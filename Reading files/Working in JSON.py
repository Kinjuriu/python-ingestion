# JSON stands for JavaScript Object Notation
# Not all python types can be encoded in JSON
# To solve this issue, python's built in JSON module
# gives you hooks to implement your own custom serialization/ de-serialization

"""Calculate average ride duration, from file with JSON object per line"""

import json
from datetime import datetime, timedelta


def parse_time(ts): #parsing a timestamp
    """
    >>> parse_time('2018-10-31T07:10:55.000Z')
    datetime.datetime(2018, 10, 31, 7, 10, 55)
    """
    # [:-1] trims Z suffix
    return datetime.fromisoformat(ts[:-1]) #fromisoformat converts it into a datetime object


def fix_pair(pair): #the fixed pair function gets a key and value as a tuple of two
    key, value = pair #we unpack here
    if key not in ('pickup', 'dropoff'):
        return pair
    return key, parse_time(value)


def pairs_hook(pairs): #called by the JSON model
    return dict(fix_pair(pair) for pair in pairs) #returns a dictionary of fixed pairs


durations = [] #create the initial list of durations
with open('taxi.jl') as fp: #open file
    for line in fp: #go for every line
        obj = json.loads(line, object_pairs_hook=pairs_hook)
        duration = obj['dropoff'] - obj['pickup']
        durations.append(duration)

avg_duration = sum(durations, timedelta()) / len(durations)
print(f'average ride duration: {avg_duration}')
