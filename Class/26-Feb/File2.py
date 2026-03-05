# general copy
import copy
g1 = [10,20,30]
l = [10,20,30,[2,3,4]]
l3 = [1,2,3,[4,5,[6,7,8]]]
g =g1
g[2] = 200
print(g1)

# shallow copy
import copy
s = g1.copy()
s[2] = 200
print(s)
print(g1)

l2 = l.copy()
l2[3][2] = 400
print(l2)
print(l)

l5 = l3.copy()
l5[3][2][1] = 700
print(l5)
print(l3)

# deep copy 
import copy
d = [1,2,3,43]
d1 = [1,2,3,[4,5,6]]
d2 = [1,2,3,[4,5,6,[7,8,9]]]

dd = copy.deepcopy(d)
d1d = copy.deepcopy(d1)
d2d = copy.deepcopy(d2)

dd[2] = 200
d1d[3][1] = 400
d2d[3][3][1] = 400
