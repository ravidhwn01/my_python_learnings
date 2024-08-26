from array import *
def printArray(arr):
   for i in range(len(arr)):
       print(arr[i],end = " ")


def main():
       myArray = array('i',[23,4,5,478,34,4,5,33])
       newArray = array(myArray.typecode,(a*a for a in myArray))
       printArray(myArray)
       print()
       printArray(newArray)



main()       