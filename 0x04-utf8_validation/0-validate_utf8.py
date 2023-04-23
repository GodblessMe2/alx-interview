#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
      Method that determines if a given data set
      represents a valid UTF-8 encoding.
    """
    number_bytes = 0

    dataSet_1 = 1 << 7
    dataSet_2 = 1 << 6

    for i in data:
        dataSet_byte = 1 << 7
        if number_bytes == 0:
            while dataSet_byte & i:
                number_bytes += 1
                dataSet_byte = dataSet_byte >> 1
            if number_bytes == 0:
                continue
            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            if not (i & dataSet_1 and not (i & dataSet_2)):
                return False
        number_bytes -= 1
    if number_bytes == 0:
        return True
    return False
