# dictionary.py
#
# Defines maxVal and minVal functions
# Inputs a dictionary from the user, or uses one of the pre-defined dictionaries
# Outputs the key paired with the max value and the key paired with the min value in the dictionary.


# TODO: COMPLETE THIS DEFINITION
def maxVal(d):
    pass

# TODO: COMPLETE THIS DEFINITION
def minVal(d):
    pass


# Dictionary containing three pre-defined dictionaries
dic = {
    1 : {
        'a' : 4,
        'b' : 4,
        'c' : 3,
        'd' : 4,
        'e' : 2,
        'f' : 3.99
    },
    2 : {
        'a' : 0,
        'b' : -1,
        'c' : 1,
        'd' : -2,
        'e' : 2,
        'f' : 0
    },
    3 : {
        'a' : 6,
        'b' : 5,
        'c' : 4,
        'd' : 3,
        'e' : 2,
        'f' : 1,
        'g' : 0
    }
}


# Inputs the list from the user as a string
l = input("Input the dictionary as key:value (no space around the colon) with spaces and/or commas between pairs.\n\n Or, input 1, 2, or 3 to use pre-defined dictionaries 1, 2, or 3\n\n")

if (l == '1'):
    d = dic[1]
elif (l == '2'):
    d = dic[2]
elif (l == '3'):
    d = dic[3]
else:
    # Turns commas into spaces for splitting
    l = l.replace(',',' ')

    # Turns the string into a list by breaking apart at spaces
    l = l.split(' ')

    # Removes any empty strings from the list (caused by putting multiple spaces and/or commas in the input)
    while '' in l:
        l.remove('')

    # Cast each entry of the list (currently a string) to a tuple (key, value) and cast the value to a float
    for i in range(len(l)):
        temp = l[i].split(':')
        temp[1] = float(temp[1])
        l[i] = tuple(temp)

    # Construct a dictionary from the list of tuples.
    d = dict(l)


# Calling the function on the tuple t and outputting the results
print("\nThe input dictionary was read as " + str(d))
key1 = maxVal(d)
print("\nThe key:value pair with the max value is " + str(key1) + " : " + str(d[key1]))
key2 = minVal(d)
print("\nThe key:value pair with the min value is " + str(key2) + " : " + str(d[key2]))