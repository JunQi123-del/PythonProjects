dummyString = "1234fdsfgrg"

print("this is the sliced string: {}".format(dummyString[3:]))

#list is mutable
numList = [1,2,3,["hello",["world"]]]

#printing world inside 3D list
print("printing world in 3d list {}".format(numList[3][1][0]))

#Dictionary
dictionaryList = {"k1":123,"k2":456}
for key in dictionaryList.keys(): 
    print("Printing the value of keys in dictionary: {}".format(dictionaryList[key]))

#Tupple 
tupleList = (1,2,3,4,5)
print("Tuple is immutable so you cannot reassign values inside a tuple: {}".format(tupleList[2]))

#set
#only stores the unique element
setList = {1,2,3,3,3,1,1,1,1}
print(setList)
listTemp = [1,2,3,2,1,2,4,5,5,5,8,7,6,6,6]
listTemp = set(listTemp)
print(listTemp)

#list comprehension
#incorporate the for loop inside a list instead to reduce code
x = [1,2,3,4]
out = []

out = [num**2 for num in x]

#same as 
#for num in x:
#    out.append(num**2)

#Function documentation
def sum():
    """
    This functions return the sum of 1 + 1
    """
    return 1+1

#Map
#Helps to reduce steps of using for loops to assign each elemtn in list to a function/lambda
def times2(int):
    return int*2

seq = [1,2,3,4,5]

print(list(map(times2,seq)))
# or 
print(list(map(lambda num:num*3,seq)))

#Filter