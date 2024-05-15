import sys



try:
    print("\nhello, my name is", sys.argv[1])
except IndexError:
    print("too few arguments")
    
# pypi.org cowsay

