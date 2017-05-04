#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    dirs = dir(hidden_4)
    for dir in dirs:
        if dir[0:2] != "__":
            print(dir)
