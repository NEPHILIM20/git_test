import numpy as np
arr1 = np.array([10, 20, 30, 40, 50])
print (arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print (arr2)

print("Hello",type(arr1))

arr3 = np.array((7,8,9,10))
print (arr3)

a = np.array([5, 10, 15, 20, 25, 30, 35])
print(a[0])

print(a[3])

print(a[2]+a[4])

print(a[1:5])

print(a[0:4])

b= np.array([1,2,3,4])
print(b.dtype)

copy = b.copy()
b[0] = 99
print(b)
print(copy)


c= np.array([1,2,3,4])
view  = c.view()
c[0] = 88
print(c)
print(view)

d = np.array([[1,2,3,4], [5,6,7,8]])
print(d.shape)

