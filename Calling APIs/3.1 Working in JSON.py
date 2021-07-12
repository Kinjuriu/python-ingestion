#One of the most common serialization formats in APIs is JSON
#Not all python types can be encoded in JSON
#You need a JSON decoder & encoder to serialize a python set into JSON

"""Example of custom JSON decoder"""
import json
from datetime import datetime
#line 9 is in JSON format, b means a bytes object

data = b''' 
{
  "from": "Wile. E. Coyote",
  "to": "ACME",
  "amount": 103.7,
  "time": "2019-08-07T12:28:39.781551"
}
'''

#fixtime takes a pair with the key, parses the string into a datetime object
def fix_time(pair):
    key, value = pair
    if key != 'time':
        return pair

    return (key, datetime.fromisoformat(value))

#object pairs hook returns a dictionary after fixing the time for every pair in the object
def object_pairs_hook(pairs):
    return dict(fix_time(pair) for pair in pairs)

#JSON has loads and dumps to work with strings or bytes
#and load and dump without the s to work with file like objects such as open files or http responses
obj = json.loads(data, object_pairs_hook=object_pairs_hook)
print(obj)
