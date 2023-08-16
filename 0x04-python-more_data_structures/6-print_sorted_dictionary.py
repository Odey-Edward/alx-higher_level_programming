def print_sorted_dictionary(a_dictionary):
    dict_keys = sorted(a_dictionary.keys())
    for key in dict_keys:
        print("{}: {}".format(key, a_dictionary[key]))
