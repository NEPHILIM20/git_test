#A
import numpy as np
arr1 = np.array([10, 20, 30, 40, 50])
print (arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print (arr2)

print(type(arr1))

arr3 = np.array((7,8,9,10))
print (arr3)

#B
a = np.array([5, 10, 15, 20, 25, 30, 35])
print(a[0])

print(a[3])

print(a[2]+a[4])

print(a[1:5])

print(a[0:4])

#C
b= np.array([1,2,3,4])
print(b.dtype)

copy = b.copy()
b[0] = 99
print(b, copy)


c= np.array([1,2,3,4])
view  = c.view()
c[0] = 88
print(c, view)

#D
d = np.array([[1,2,3,4], [5,6,7,8]])
print(d.shape)

oned = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(oned.reshape(4,3))
print(oned.reshape(2,3,2))

#S
print(np.array([1,2,3,4,5], ndmin=5))

#E
e = np.array([2,4,6])

for x in e:
    print(x)

#S
f = np.array([[1,2], [3,4]])
for x in f:
    for y in x:
        print(y)

#S
g= np.array([10,20,30])
for index, x in np.ndenumerate(g):
    print(index, x)

#F
x = np.array([1,2,3])
y = np.array([4,5,6])

print(np.concatenate((x,y)))

print(np.stack((x,y), axis=1))

print(np.vstack((x,y)))

split = np.array([1,2,3,4,5,6])
print(np.array_split(split, 3))

#G
h = np.array([1,4,2,4,5,4])
print(np.where(h == 4))

i = np.array([9,3,7,1])
print(np.sort(i))

#S
j= np.array([1,2,3,4,5,6,7,8])
filter = j%2 == 0
print(np.array(j[filter]))

#H
from numpy import random

print(random.randint(100, size=(5)))

print(random.choice([3,5,7,9]))

p = np.array([10,20,30])
q = np.array([1,2,3])

print(np.add(p,q))