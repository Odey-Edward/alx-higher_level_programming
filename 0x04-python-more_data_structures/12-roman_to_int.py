#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):

        # The roman charcter an it associated value
        roman_dict = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }

        result = 0
        prev_key = 0

        for idx in range(len(roman_string)):
            for key in list(roman_dict):

                # check if is a valid roman character
                if roman_string[idx].upper() == key:
                    '''
                    Do necessary computation if the iteration
                    is not in first index
                    '''
                    if roman_string[idx].upper() == key and idx > 0:
                        if roman_dict[key] == prev_key:
                            result = result + roman_dict[key]
                        elif roman_dict[key] > prev_key:
                            result = roman_dict[key] - result
                        elif prev_key > roman_dict[key]:
                            result = result + roman_dict[key]
                    # Handle iteration on the first index
                    else:
                        result = result + roman_dict[key]

                    # save the previous roman character
                    prev_key = roman_dict[key]

                if result > 3999:
                    return (0)

        return (result)
    return (0)
