# myArray = [24, 16, 71, 78, 90]
#
#
# #Bubble sort Algorithm
#
# n = len(myArray) #5 returned value of len ()
# for i in range (n): #cycles through values 1 - 4
#     for j in range(0, n - i - 1): #cycles through pairs of element in the data set
#         if myArray[j] > myArray[j+1]:
#             myArray[j], myArray[j+1] = myArray[j+1], myArray[j]
# print(myArray)


#Selection sort algorithm

# myArray1 = [24, 16, 71, 78, 90]
# print("I am printing the unsortred array: ")
# print(myArray1)
# #Algorithm Proper
# for i in range (len(myArray1)):
#     min_idx = i
#     for j in range (i + 1, len(myArray1)):
#         if myArray1[min_idx] > myArray1[j]:
#             min_idx = j
#             #myArray1[i] is the first index of the selection
#             #myArray[min_idx] is the index of the minimum value for
#             myArray1[i], myArray1[min_idx] = myArray1[min_idx], myArray1[i]
# print("The sorted array using Selection sort1111111")
# print(myArray1)

# #Insertion Sort Algorithm
# myArray2 = [24, 16, 71, 78, 90]
# print("I am printing the unsorted array: ")
# print(myArray2)
# #Insertion Sort Proper
# for i in range (1, len(myArray2)):
#     key = myArray2[i]
#     j = i-1
#     #move elements that are greater than the key to one position ahead of
#     #their current position
#     while j >= 0 and key < myArray2[j]:
#         myArray2[j +1] = myArray2[j]
#         j -=1
#     myArray2[j+1] = key
# print("The sortred array using Insertion Array")
# print(myArray2)


Array1 = [23, 89, 7, 56, 44]


#1

n = len(Array1)
for i in range (n):
    for j in range(0, n - i - 1):
        if Array1[j] > Array1[j+1]:
            Array1[j], Array1[j+1] = Array1[j+1], Array1[j]
print("Bubble Sort Algorithm in Ascending Order")
print(Array1)


#2

Array2 = [12, 78, 91, 34, 62]

for i in range (1, len(Array2)):
    key = Array2[i]
    j = i-1
    while j >= 0 and key < Array2[j]:
        Array2[j +1] = Array2[j]
        j -=1
    Array2[j+1] = key
print("Insertion Sort Algorithm in Ascending Order")
print(Array2)

#3

Array3 = [5, 99, 48, 15, 67]

for i in range (len (Array3)):
    min_idx = i
    for j in range (i+1, len(Array3)):
        if Array3[min_idx] < Array3[j]:
            min_idx = j
            Array3[i-1], Array3[min_idx] = Array3[min_idx], Array3[i-1]
print("Selection sort algorithm in Descending Order")
print(Array3)

#4

Array4 = [38, 82, 25,74, 13]
for i in range (1, len(Array4)):
    key = Array4[i]
    j = i-1
    while j >= 0 and key > Array4[j]:
        Array4[j +1] = Array4[j]
        j -=1
    Array4[j+1] = key
print("Insertion sort algorithm in Descending Order")
print(Array4)

#5

Array5 = [7,56,91,34, 48,15,25,74]
n = len(Array5)
for i in range (n):
    for j in range(0, n - i - 1):
        if Array5[j] > Array5[j+1]:
            Array5[j], Array5[j+1] = Array5[j+1], Array5[j]
print("Bubble Sort Algorithm in Ascending Order")
print(Array5)

for i in range (n):
    for j in range(0, n - i - 1):
        if Array5[j] < Array5[j+1]:
            Array5[j], Array5[j+1] = Array5[j+1], Array5[j]
print("Bubble sort algorithm in Descending Order")
print(Array5)


Array6 = [12, 78, 91, 34, 62, 5, 99 , 48 , 15, 67, 38, 82, 25, 74, 13]
for i in range (len(Array6)):
    min_idx = i
    for j in range (i + 1, len(Array6)):
        if Array6[min_idx] > Array6[j]:
            min_idx = j
            Array6[i], Array6[min_idx] = Array6[min_idx], Array6[i]
print("This is Selection Algorithm in Asencding order")
print(Array6)








