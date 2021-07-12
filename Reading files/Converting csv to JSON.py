"""Convert CSV to JSON (one object per line)"""
import bz2 #we import bz2 since the file is compressed
import csv #processes the csv
import json
from collections import namedtuple
from datetime import datetime
import pandas as pd

Column = namedtuple('Column', 'src dest convert')


def parse_timestamp(text):
    return datetime.strptime(text, '%Y-%m-%d %H:%M:%S')

#We convert from text to the right python type
columns = [
    Column('VendorID', 'vendor_id', int),
    Column('passenger_count', 'num_passengers', int),
    Column('tip_amount', 'tip', float),
    Column('total_amount', 'price', float),
    Column('tpep_dropoff_datetime', 'dropoff_time', parse_timestamp),
    Column('tpep_pickup_datetime', 'pickup_time', parse_timestamp),
    Column('trip_distance', 'distance', float),
]


def iter_records(file_name): #iterates over the lines
    with bz2.open(file_name, 'rt') as fp:
        reader = csv.DictReader(fp)
        for csv_record in reader:
            record = {}
            for col in columns:
                value = csv_record[col.src]
                record[col.dest] = col.convert(value)
            yield record

#JSON does not support date time objects, so we need to encode as string
def encode_time(obj):
    if not isinstance(obj, datetime):
        return obj
    return obj.isoformat()


with open('taxi.jl', 'w') as out:
    for record in iter_records('taxi.csv.bz2'):
        data = json.dumps(record, default=encode_time)
        out.write(f'{data}\n')


