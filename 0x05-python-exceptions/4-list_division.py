#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(list_length):
        try:
            newList.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            newList.append(0)
            print("wrong type")
        except ZeroDivisionError:
            newList.append(0)
            print("division by 0")
        except IndexError:
            newList.append(0)
            print("out of range")
    return (newList)
