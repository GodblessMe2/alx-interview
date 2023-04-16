#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''


import sys

dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}
total_file_size = 0
counter = 0

try:
    for line in sys.stdin:
        parsed_line = line.split(" ")
        if len(parsed_line) > 4:
            # status code
            code = parsed_line[-2]
            size = int(parsed_line[-1])
            if code in dict_sc.keys():
                dict_sc[code] += 1
            total_file_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_file_size))
            for key, value in sorted(dict_sc.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(dict_sc.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
