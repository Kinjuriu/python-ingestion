# CSV can be compressed a lot
# We are using the New York taxi data
# In python we use two options to load csv, using the built- in csv model & pandas

"""Load and convert data from csv file using python built-in csv module"""
import bz2
import csv
from collections import namedtuple
from datetime import datetime

Column = namedtuple('Column', 'src dest convert')


def parse_timestamp(text):
    return datetime.strptime(text, '%Y-%m-%d %H:%M:%S')


columns = [       #since we have a header row, we use dictionary reader- consumes at most one line
    Column('VendorID', 'vendor_id', int),  # allowing us to process huge files without blowing our computer memory
    Column('passenger_count', 'num_passengers', int), #Everything in csv is text
    Column('tip_amount', 'price', float),  #we need a way to convert text fields into the right data type
    Column('total_amount', 'price', float),
    Column('tpep_dropoff_datetime', 'dropoff_time', parse_timestamp),
    Column('tpep_dropoff_datetime', 'pickup_time', parse_timestamp),
    Column('trip_distance', 'distance', float),
]

def iter_records(file_name): #opens the file
    with bz2.open(file_name, 'rt') as fp: #we open the file in text mode cause csv works only with text
        reader = csv.DictReader(fp)  #creates a reader
        for csv_record in reader:
            record = {}  #for every record it creates an empty dictionary
            for col in columns:  #for every column it gets a converter
                value = csv_record[col.src]
                record[col.dest] = col.convert(value)  #applies converter to the value
            yield record #we use a generator, returning one record at a time avoiding memory blowout

#her is an example
def example():
    from pprint import pprint ##we import pprint to print something nice

    for i, record in enumerate(iter_records('taxi.csv.bz2')):
        if i >=10:  #we iterate over the records to show the first 10 lines then we print them out
            break
        pprint(record)

example()

