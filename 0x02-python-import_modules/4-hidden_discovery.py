#!/usr/bin/python3
if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4 *

    allf = dir()
    for i in range(0,len(allf)):
        if allf[i]{:2} != "__":
            print("(:s)".format(allf[i]))
