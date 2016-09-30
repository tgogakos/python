#!/usr/bin/python

class Duck():
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):
        print("i can quack")

    def walk(self):
        print("i can walk")

    def get_properties(self):
        return self.properties
    
    def get_property(self, key):
        return self.properties.get(key, None)

    @property
    def color(self):
        return self.properties.get('color', None) 

    @color.setter
    def color(self, c):
        self.properties['color'] = c 

    @color.deleter
    def color(self):
        del self.properties['color']

def main():
    donald = Duck(color = "blue", fur = "white")
    print(donald.get_property("color"))
    print(donald.get_properties())

    
if __name__ == "__main__":main()
