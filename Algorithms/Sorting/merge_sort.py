def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2 #Divides Here
        left = myList[:mid] #Left of code to mid
        right = myList[mid:] #Mid of code to right
        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

myList = [54,26,93,17,77,31,33,47,92,44,55,20,5342,1,90,5481,687,22,53,54,12]
mergeSort(myList) # Sends list to function
print(myList)



# https://www.educative.io/edpresso/merge-sort-in-python