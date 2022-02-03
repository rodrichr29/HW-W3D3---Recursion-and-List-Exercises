# Exercise 1
# Problem
places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']
# Solution
places = list(' '.join(places).split())                 
print(places)

# Exercise 2
# Problem
authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]
#Solution
authors.sort(key = lambda x: x.split(" "))
print(authors)

# Exercise 3
# Problem
places_1 = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]
# Solution
temperture_conversion = map(lambda x: (float(9)/5)*x + 32, places_1[1:])
print(places_1)
# Exercise 4 
# Problem

# 1, 1, 2, 3, 5, 8, 11

# {
#     '1': 1,
#     '2': 1,
#     '3': 2,
#     '4': 3,
#     '5': 5,
#     ,...
# }

# def fib():
#    pass
# Solution
def fib():
    x = 0 # vars
    while True:
        yield x  # start of generator

for num in range(12):
    print('{x}:{x}'.format(x = num))
