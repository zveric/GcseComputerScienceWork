def insertionSort(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      # Move elements of arr[0..i-1], that are greater
      #than key,
      # to one position ahead of their current position
      j = i-1 # j is the seccond to last item (i think)
      while j >=0 and key < arr[j] :# while j is not below 0  and key is less than j, keeps looping until sorted
         arr[j+1] = arr[j]# position above j becomes j
         j -= 1# j moves down a position
      arr[j+1] = key# key is the positionin front of j
# main
arr = ['t','u','t','o','r','i','a','l']
insertionSort(arr)
print ("The sorted array is:")
for i in range(len(arr)):
   print (arr[i])



