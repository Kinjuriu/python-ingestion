# Unstructured text is like: Ride of 1 passenger started at 2018-10-31T07:10:55 and paid $20.54
# So we use a site called pythex to change this line to construct a regular expression
# So now we get something like this: of (\d+).*started at ([^ ]+).*paid \$(\d+\.\d+)


"""Convert unstructured ride text to JSON"""
import bz2
import logging
import re #regular expression
from datetime import datetime


def parse_line(line): #gets one line and returns the count, the start and the amount
    # Example:
    # Ride of 1 passenger started at 2018-10-31T07:10:55 and paid $20.54
    match = re.search(
        r'(\d+) pass.*started at ([^ ]+).*paid \$(\d+\.\d+)',
        line)
    if not match:
        return None

    return {
        'count': int(match.group(1)),
        'start': datetime.fromisoformat(match.group(2)),
        'amount': float(match.group(3)),
    }
    #here we return a dictionary

def iter_rides(file_name):
    with bz2.open(file_name, 'rt') as fp:
        for lnum, line in enumerate(fp, 1):
            record = parse_line(line)
            if not record:
                logging.warning('%s: cannot parse line', lnum)
                continue
            yield record


# Example
if __name__ == '__main__':
    from pprint import pprint

    for n, ride in enumerate(iter_rides('taxi.log.bz2')):
        if n > 5:
            break
        pprint(ride)