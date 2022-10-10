# same_tuple.py
#
# Defines isConstant function
# Inputs a tuple from the user
# Outputs True if all elements of the tuple are the same, False otherwise.


# TODO: COMPLETE THIS DEFINITION
def isConstant(t):
    pass



# Inputs the list from the user as a string
l = input("Input the tuple as numbers separated by spaces and/or commas.\n\n")

# Turns commas into spaces for splitting
l = l.replace(',',' ')

# Turns the string into a list by breaking apart at spaces
l = l.split(' ')

# Removes any empty strings from the list (caused by putting multiple spaces and/or commas in the input)
while '' in l:
    l.remove('')

# Cast each entry of the list (currently a string) to a float
for i in range(len(l)):
    l[i] = float(l[i])

# Construct a tuple from the list.
t = tuple(l)


# Calling the function on the tuple t and outputting the results
print("\nThe input tuple was read as " + str(t))
print("Is the tuple constant? " + str(isConstant(t)))