#!/usr/bin/python

class inclusive_range():
    def __init__(self, *args):
        numargs = len(args)
        
        if numargs < 1:
            raise TypeError("at least one")
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        elif numargs == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        else:
            raise TypeError("too many args")

#this makes the object iterable 
    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i 
            i += self.step

def main():
    for i in inclusive_range():
        print(i, end = "\n")

#def main():
#    s = "AAATTTGGGCCC"
#    o = range(0, len(s), 2)
#    for i in o: 
#        print(s[i], end=" ")




if __name__ == "__main__":main()
