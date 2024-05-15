
names = [ 'Dave', 'Paula', 'Thomas', 'Lewis' ]
a = names[2]
print(a)
print(names)
names[2] = "tom"
print(names)

# append the names
names.append("alexa")
print(names)

names.insert(2,"paluguna")
print(names)


for name in names:
    print(name, sep=" ")


    '''
    An empty list is created in one of two ways:
names = []        # An empty list
names = list()    # An empty list
    '''