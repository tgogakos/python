#!/usr/bin/python
import sys

def main():
    #getting information of webpage
    import urllib.request
    page = urllib.request.urlopen('http://www.rockefeller.edu')
    for line in page:
        print(str(line, encoding = "utf_8"), end = " ")
 
 
    
        



if __name__=="__main__":main()
