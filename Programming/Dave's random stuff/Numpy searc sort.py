# this code returns all index postitions
# where 4 is, which is shown by printin x

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# _____________

#this code returns index postitions
#where all values are even

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

#________________

#this code is werid
#it requires a sorted list

import numpy as np
arr = np.array([6, 7, 8, 9,])
x = np.searchsorted(arr, 8)
print(x)

#Sorts list by default, e.g alphabeticall, 
#or by number for each digit, so 11 goes before 3 
# becasue 1 is less than 3 (1<3)

cars = ['Ford', 'BMW', 'Volvo', 'Aston', '11', '3']
cars.sort()
print(cars)





