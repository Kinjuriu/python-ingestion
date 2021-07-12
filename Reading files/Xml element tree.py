"""Load rides data from xml"""

#There are two ways of reading xml,
#1.DOM- Document Object Memory- loading everything into memory
#2.SAX- Simple API for XML- Iterative(great for big files)

#two main libraries for working with XML are the built-in ElementTree(in the standard library)
# and lxml- third party

import bz2
import xml.etree.ElementTree as xml

import pandas as pd

# data conversions- we need to convert everything manually
conversion = [
    ('vendor', int),
    ('people', int),
    ('tip', float),
    ('price', float),
    ('pickup', pd.to_datetime),
    ('dropoff', pd.to_datetime),
    ('distance', float),
]

def iter_rides(file_name): #open the file
    with bz2.open(file_name, 'rt') as fp:
        tree = xml.parse(fp) #load the whole file into memory and parse it

    rides = tree.getroot() #get the root of the tree
    for elem in rides:
        record = {}
        for tag, func in conversion:
            text = elem.find(tag).text
            record [tag] = func(text)
        yield record

def load_xml(file_name):  #define load xml
    records = iter_rides(file_name)  #we use our function to generate the records
    return pd.DataFrame.from_records(records) ##we use pandas dataframe from records to create a dataframe

# Example
if __name__ == '__main__':
    df = load_xml('taxi.xml.bz2')
    print(df.dtypes)
    print(df.head())
