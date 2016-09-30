#!/usr/bin/python

def main():
    input = open("test")
    out = open("new", "w")

    for index, line in enumerate(input):
        print(index, "\t",  line, end="", file = out)

if __name__ == "__main__":main()
