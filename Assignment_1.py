Assignment Solution [ List Problems]
1.	Write a function to return a list with all the duplicate elements from the list
def findDuplicateElements(inputList):
    # initiate an empty dictionary to count the occurrence of each elements
    # initiate an empty list to store all the duplicate elements only and return to the function
    dictionaryForElementsCounts = {}
    listOfDuplicateElements = []

    # Iterate through the input list and store the occurrences of each element in dictionary
    for element in inputList:
        if element in dictionaryForElementsCounts:
            dictionaryForElementsCounts[element] += 1
        else:
            dictionaryForElementsCounts[element] = 1

    # Add all the duplicate elements in the list ( which are having counts > 1 )
    for element, count in dictionaryForElementsCounts.items():
        if count > 1:
            listOfDuplicateElements.append(element)

    return listOfDuplicateElements

    # Calling and execute the function
inputList =[1, 2, 3, 1, 7, 3,4, 2, 5, 6,]
ansList = findDuplicateElements(inputList)
print(ansList)


2.	Write a function to return a list with all the singly occurred elements ( which appear only once ) from the list
def findSinglyOccurredElements(inputList):
    # initiate an empty dictionary to count the occurrence of each elements
    # initiate an empty list to store all the duplicate elements only and return to the function
    dictionaryForElementsCounts = {}
    listOfSinglyOccuredElements = []

    # Iterate through the input list and store the occurrences of each element in dictionary
    for element in inputList:
        if element in dictionaryForElementsCounts:
            dictionaryForElementsCounts[element] += 1
        else:
            dictionaryForElementsCounts[element] = 1

    # Add all the duplicate elements in the list ( which are having counts > 1 )
    for element, count in dictionaryForElementsCounts.items():
        if count == 1:
            listOfSinglyOccuredElements.append(element)

    return listOfSinglyOccuredElements

# Calling and execute the function
inputList =[1, 2, 3, 1, 7, 3,4, 2, 5, 6,]
ansList = findSinglyOccurredElements (inputList)
print(ansList)



3.	Write a Python program to find the sum of all elements in the list and print.
def printSumOfListElements(inputList):
    sum = 0
    # Iterate through the input list and keep ading to sum variable
    for element in inputList:
        sum = sum + element
    print("sum of elements from the given list is :",sum)
# Calling and execute the function
inputList =[1,2,3,4,5]
printSumOfListElements (inputList)

4.	Write a program to find the largest number in the list and return.
def printTheBiggestNumber(inputList):
    biggestNumber = inputList[0]
    # Iterate through the list and compare find the biggest number
    for element in inputList:
        if biggestNumber < element:
            biggestNumber = element
    print("The biggest number from the given list is :",biggestNumber)
# Calling and execute the function
inputList =[1,2,9,3,4,5]
printTheBiggestNumber (inputList)

5.	Remove Duplicates from a List and return the list
def removeDuplicates(inputList):
    return set(inputList)
inputList =[1,2,9,3,4,5,1,2,3]
print(removeDuplicates (inputList))

6.	Find the Second Largest Element and print.
def secondLargestNumber(inputList):
    inputList.sort()
    print("After Sorting the list : ",inputList)
    return inputList[-2]

inputList =[1,2,9,3,4,5,7,1,2,3]
print(secondLargestNumber (inputList))


