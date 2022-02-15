#import vector
#print(vector.a)

from vector import Vector

a_vec = Vector([3,4])
b_vec = Vector([4,5])
print(a_vec)
print(str(a_vec))
print(len(a_vec))
print(a_vec.length()) #This is the normal one
print(Vector.__len__(a_vec))
print(Vector.length(a_vec))

try:    #This is called a try catch
    c_vec = Vector(["a","b"])
    print(Vector.length(c_vec))
    print(c_vec.length())
except:
    print("failed to create valid vector")

print(a_vec+b_vec)
d_vec = a_vec.copy()
print(d_vec)
d_vec[0] = 90
print(d_vec)
