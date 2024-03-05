# Converting from Integer to string of any base
def to_string(n, base):

    baseChars = "0123456789ABCDEF"
    
    # With the base case commented, this function will result in a stack-overflow error
    #if n < base:
        #return baseChars[n]

    return to_string(n // base, base) + baseChars[n % base]

# Run above code 1
print(to_string(9, 2))

# Converting a JSON string into a python dictionary
import json
def jsonToPy(str): 

    # without a try catch block, any input string that is not a JSON string will return an error
    pyDict = json.loads(str)

    return pyDict

# Run above code 2
#print(jsonToPy('( "name":"Lucy", "age":25, "city":"New York")'))

# Opening an existing file
def fileReader():

    # trying to open a non-existing file to read will cause an error
    f = open("testfile2.txt", "r")

    print(f.read())

# Run above code 3
#fileReader()

# Given an index, return the value of the stored in a local array
def getElement(idx):
    lst = [1, 1, 2, 3, 5, 8, 13]

    # without checking the input index, may cause an indexError

    return lst[idx]

# Run above code 4
#print(getElement(9))