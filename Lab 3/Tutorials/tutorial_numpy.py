import numpy as np
a = np.array([1,2, 3])
a = np.array([(1,2,3), (4,5,6)])

myList = [1,2,3]
a = np.array(myList)

a = np.zeros((2,2))
a = np.ones((3,3))

a = np.array([(1,2,3),(4,5,6)])
a.reshape(3,2)

a = np.array([(1,2,3),(4,5,6)])
b = a.flatten()
b.shape # (6,) NOT (6,1)!
a = np.array([1,2,3,4,5,6,7])
b = np.resize(a, (1,4)) # array([[1, 2, 3, 4]])
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.hstack((a,b))
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.vstack((a,b))
a = np.arange(1,11,1)
a = np.linspace(1.0,5.0,10, False)
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a[0] # This gives us the first row of a
a[2] # This gives us the third row of a
a[:,1] # this gives us the second column of a
a[2][2] # this gives us the value of a(2,2), which is 9 here

array1 = np.array([0, 10, 4, 12])
array1a = array1 - 20
array1b = array1a.shape

array2 = np.array([[0,10, 4, 12], [1, 20, 3, 41]])

#5th element on 2nd row arr[1,4]
array2_temp = array2.reshape(4,2)
array2_temp = np.resize(array2_temp, (3,2))
array2_new = array2_temp[1:4,:]


array3 = np.hstack((array1, array1))
array3 = np.vstack((array3, array3, array3, array3))
array4a = np.arange(-3,15, 6)
array4b = np.arange(-7, -19, -2)
array6 = np.zeros((3,4))
array6[1, 0] = 0
array6[0] = [12, 3, 1, 2]
array6[:, 1] = [3, 0, 2]
array6[2, :2] = [4, 2]
array6[2, 2:] = [3, 1]
array6[:, 2] = [1,1, 3]
array6[1, 3] = 2


array5 = np.linspace(0, 100, 49, True)
print(" array1 ", array1) #done
print(" array1a ", array1a)
print(" array1b ", array1b)
print(" array2 ", array2_new)
print(" array3 ", array3) #done?
print(" array4a ", array4a)
print(" array4b ", array4b)
print(" array5 ", array5)
print(" array6 ", array6)#done