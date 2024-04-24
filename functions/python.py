#print("languges:\n\tpython\n\tC\n\tjavaScript")

# python  progam for beginerr
"""
name = input("what's your name ? ").strip().title()
age = input("what is ur age")
print(" hey my name, " + name + " my age is " + age )


variable String = str
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str


print(f"hellow, {name}")
print(str.capitalize(name))

name = name.strip().title()
print(name)

# split the user name into first name && last name
print(name.split())


x = input("enter the first number") 
y = input("enter the second number")

z = int(x) + int(y) 

print(z)

"""


#use a varible to print a person namem and then message to that person
first_name = "paluguna"
last_name = "kadupukotla"

full_name = f"{first_name} {last_name}"
print(full_name.title())
message = f"Hello, {full_name.title()}"
print(message)

# print name in lower case
print(message.lower())

print(message.upper())

#Adding an quote
quote =   ' “A person who never made a mistake never tried anything new.” '

print(f"Albert Einstein once said,{quote.title()}")

# Adding Whitespace to Strings with Tabs or Newlines
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJava\njavascritp")


#stripping of white spaces

favorate_lang = " python "
print(favorate_lang)
print(favorate_lang.strip())


# remove prefix 

nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix("https://"))


#Numbers

n: int = 1000000000
print(n)
print(f'{n:_}')
print(f'{n:,}')

# Multiple assingment

x,y,z = 1,2,3
print(x+y+z)

# Introduction to list

bicycles = ['trex','cannodale', 'redline', 'speciallized']

print(bicycles)

# Accessing Elements in a List
print(bicycles[0])
print(bicycles[0].title())

print(bicycles[-1])

message = f"My first bike was a {bicycles[0].title()}"

print(message)

motocycles = ['honda','ducati','suzuki','yamaha']
print(motocycles[0])
motocycles[0] = 'herohonda'
print(motocycles[0])


#Adding element to a list by using append
motocycles.append('buguati')
print(motocycles)


motocycles.append('bmw')
motocycles.append('vw')
motocycles.append('mercedes')
motocycles.append('acura')
print(motocycles)

# insert we can add any were in the list
motocycles.insert(0,'lexus')
print(motocycles)
motocycles.insert(5,'lexuss')
print(motocycles)

del motocycles[5]
print(motocycles)



# removing elements using pop method which will be deleted the top one in the list stack

popped_motocyles = motocycles.pop()
print(popped_motocyles)

print(motocycles)

last_owned = motocycles.pop()

print(f"the last owned motocycle i owned was a {last_owned.title()}")

first_owned = motocycles.pop(0)
print(f"the first owned vehicle was a {first_owned.title()}.")


#remvoing by an value

# before removing
print(motocycles)
motocycles.remove('herohonda')
print(motocycles)

too_expensive ="ducati"
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA {too_expensive.title()} is too expensive fo me")

print("Here is the original list:")
print(motocycles)

motocycles.sort()
print("\nHere is the sorted list")
print(sorted(motocycles))


#check this again
print("\nHere is the orignal list again")
print(motocycles.sort(reverse=True))

# find a length of the list
print(len(motocycles))

# looping through entire list

motocars = ['lexus', 'herohonda', 'ducati', 'suzuki', 'yamaha', 'buguati', 'bmw', 'vw', 'mercedes', 'acura']

for moto in motocars:
    print(f"{moto.title()}, that was a nice cars")
    print(f"I can wait to see your next car, {moto.title()}.\n")
print("Thank you, everyone. That was a great magic show!")    

#range function

for value in range(1,5):
    print(value)


# Using range() to Make a List of Numbers
nunbers = list(range(1,6))
print(nunbers)

even_numbes = list(range(2,11,3))
print(even_numbes)

squares =[]
for value in range(1,11): # for the range between 1 t0 10
    square = value **2    # for each value we are squaring and storing the value in square
    squares.append(square) # we are adding square to the list 

print(squares)    

for values in range(1,21):
    print(values)

# odd numbers in the list
# odd =[]
# for valve in range(1,20,2):
#       val =( valve /2) == 0:
#       if(val ==0):
#         odd.append(val)
# print(odd)
odd =[]
odd_nubers = list(range(1,20,2))
odd.append(odd_nubers)
print(odd)


multiples =[]
for value in range(1,31): # for the range between 1 t0 10
    multi = (3 * value)    # for each value we are squaring and storing the value in square
    multiples.append(multi) # we are adding square to the list 

print(multiples)    
