from numpy import*

arr1=array ([[1,2],
        [3,4]])
        
print('printing size of the array-' ,arr1.size)

print('printing dimension of the array-' ,arr1.ndim)

print('flatten the array')
arr2=arr1.flatten
print(arr2)

print('reshaping the array')
print(arr2.reshape(1,1))
