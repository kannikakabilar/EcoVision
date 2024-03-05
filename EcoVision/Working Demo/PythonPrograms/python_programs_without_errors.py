# Converting from Integer to string of any base
def to_string(n, base):
    # Character set used for the conversion in hexadecimal format
    baseChars = "0123456789ABCDEF"
    
    # base case that prevents this recursive function from going into stack-overflow
    if n < base:
        # Check if the number, n is less than the specified base => return the corresponding char
        return baseChars[n]

    else:
        # Else n is greater than or equal to the base, make a recursive call to convert 
        # the quotient (n // base) and concatenate it with the remainder from char set
        return to_string(n // base, base) + baseChars[n % base]

# Run above code 1
#print(to_string(9, 2))

# Converting a JSON string into a python dictionary
import json
def jsonToPy(str): # input string must be in JSON string format to prevent any errors from being thrown
    # use json library to convert the JSON string to a python dictionary and return it
    pyDict = json.loads(str)

    return pyDict

# Run above code 2
#print(jsonToPy('{ "name":"Lucy", "age":25, "city":"New York"}'))

# Opening an existing file
def fileReader():
    f = open("testfile.txt", "r")

    print(f.read())

    f.close()

# Run above code 3
#fileReader()

# Given an index, return the value of the stored in a local array
def getElement(idx):
    lst = [1, 1, 2, 3, 5, 8, 13]

    # without checking the input index, it may result in a indexError
    if(idx<0):
        return lst[0]
    elif(idx>=len(lst)):
        return lst[len(lst)-1]
    else:
        return lst[idx]

# Run above code 4
#print(getElement(4))