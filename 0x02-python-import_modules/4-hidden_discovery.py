#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for element in dir(hidden_4):
        if not element.startswith("__"):
            print("{}".format(element))
