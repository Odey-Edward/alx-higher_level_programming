def print_sorted_dictionary(a_dictionary):
    dict_keys = sorted(a_dictionary)
    for key in dict_keys:
        print("{:s}: {}".format(key, a_dictionary[key]))
