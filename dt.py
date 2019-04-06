#dt.py

import sys
import pprint

class sample(dict):
    def __init__(self, data):
        super().__init__(data)



def parse_data(file_name):
    '''
     This function reads a file and parses data
     finally, return a list: [{attribute:value, a:v, ...}, {a:v, ...}, {a:v, ...}, ...]
     The operation is:
        1. parsing first line in file then get a list which has name of attributes as element
        2. parsing next line then get a parsed data
        3. zip(attributes, parsed data), it returns a list has (attribute, parsed data)s as element
        4. creates new sample that is dictionary has attribute:data as key:value
        5. append new sample to result list
        6. Iterates step 2~4 until meet EOF
        7. return a list: [{attribute:value, a:v, ...}, {a:v, ...}, {a:v, ...}, ...]
    '''
    try:
        with open(file_name, 'rt') as f:
            result = []
            attributes = f.readline().strip().split('\t')
            for line in f.readlines():
               data_parsed = line.strip().split('\t')
               new_sample = sample(zip(attributes, data_parsed))
               result.append(new_sample)
        return result
    except IOError as err:
        print('File error: '+ str(err))
    except Exception as other:
        print('Somethig else broke:'+ str(other))


file_name = sys.argv[1]
data = parse_data(file_name)
pprint.pprint(data)

    
