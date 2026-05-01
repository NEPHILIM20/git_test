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
print(b)
print(copy)


c= np.array([1,2,3,4])
view  = c.view()
c[0] = 88
print(c)
print(view)

#D
d = np.array([[1,2,3,4], [5,6,7,8]])
print(d.shape)

oned = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
shaped = oned.reshape(4,3)
print(shaped)

shaped2 = oned.reshape(2,3,2)
print(shaped2)

#SACRIFICE
ndmin = np.array([1,2,3,4,5], ndmin=5)
print(ndmin.shape)

#E
e = np.array([2,4,6])

for x in e:
    print(x)

#SACRIFICE
f = np.array([[1,2], [3,4]])
for x in f:
    for y in x:
        print(y)

#SACRIFICE
g= np.array([10,20,30])
for index, x in np.ndenumerate(g):
    print(index, x)

x = np.array([1,2,3])
y = np.array([4,5,6])

#F
join = np.concatenate((x,y))
print(join)

stack = np.stack((x,y), axis=1)
print(stack)

stack2 = np.vstack((x,y))
print(stack2)

split = np.array([1,2,3,4,5,6])

threesplit = np.array_split(split, 3)
print(threesplit)

#G
h = np.array([1,4,2,4,5,4])
findindex = np.where(h == 4)
print(findindex)

i = np.array([9,3,7,1])
sort = np.sort(i)
print(sort)

j= np.array([1,2,3,4,5,6,7,8])
filter = j%2 == 0
print(j[filter])

#H

from numpy import random

random1 = random.randint(100, size=(5))
print(random1)

random2 = random.choice([3,5,7,9])
print(random2)

p = np.array([10,20,30])
q = np.array([1,2,3])

add = np.add(p,q)
print(add)