#!/usr/bin/python3
if __name__ == "__main__":

    import hidden_4
    modyule = dir(hidden_4)
    for name in modyule:
        if name[0:2] != "__":
            print("{:s}".format(name))
