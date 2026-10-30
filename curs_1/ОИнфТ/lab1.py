import numpy as np
import matplotlib.pyplot as plt


def print_vector(vector):
    values = "  ".join(f"{value:10.4f}" for value in vector)
    print(f"[ {values} ]")


class MZ:

    def __init__(self, A, x, b, e):
        self.A = A
        self.x = x
        self.b = b
        self.e = e

    def solve(self):
        
        k = 0
        e_max = 1.
        LU = np.tril(self.A, -1) + np.triu(self.A, 1)
        x_next = np.copy(self.x)
        
        while e_max > self.e:
            
            self.x = x_next.copy()
            
            for index, row_LU in enumerate(LU):
                x_next[index] = 1/self.A[index][index] * (self.b[index] - np.dot(row_LU, x_next))
                
            e_max = np.max(np.abs(x_next - self.x))
            
            print(f"{k}) e_max = {e_max} - ", end="")
            print_vector(x_next)
            
            k += 1

#Входные параметры 

A = np.array([
    [-2.17, 1, 0, 0, 0],
    [1, -2, 1, 0, 0],
    [0, 1, -2, 1, 0],
    [0, 0, 1, -2, 1],
    [0, 0, 0, 1, -2.17]
])
x = [0, 0, 0, 0, 0]
b = [0, 6, 6, 6, 0]
e = 1e-4

mz = MZ(A, x, b, e)
print("--- Solution of SLAE by the method MZ ---")
print("`Input data:")
print(f"e = {mz.e}, ")
print("\nA = ")
for vec in mz.A:
    print_vector(vec)
    
print("\nb = ", end="")
print_vector(mz.b)

print("\nx = ", end="")
print_vector(mz.x)

print("-- Start solve --")
mz.solve()
