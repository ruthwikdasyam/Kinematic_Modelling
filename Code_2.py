import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

l2, θ2, l3, t = symbols('l2 θ2 l3 t')   #declating l2 θ2 l3 t as constants 
init_printing(use_unicode=True)

θ1 = Function("θ1")(t)   #declaring θ1 as a function of t
l1 = Function("l1")(t)   #declaring l1 as a function of t
θ3 = Function("θ3")(t)   #declaring θ3 as a function of t

#x, y, θ in terms of l1, l2, l3, θ1, θ2, θ3 as provided in the documentation

x = l1*cos(θ1) + l2*cos(θ1+θ2) + l3*cos(θ1+θ2+θ3)
y = l1*sin(θ1) + l2*sin(θ1+θ2) + l3*sin(θ1+θ2+θ3)
θ = θ1+θ2+θ3

#Differentiating x,y,θ wrt t

x_dot = diff(x, t)  
y_dot = diff(y, t)
θ_dot = diff(θ, t)   #x_dot, y_dot, θ_dot values are obtained

# print("x_dot = ", x_dot)
# print("y_dot = ", y_dot)
# print("θ_dot = ", θ_dot)

#By performing the factorization, the below represention of these equations are obtained

A= Matrix(3,3, [cos(θ1), -l2*sin(θ2+θ1)-l3*sin(θ2+θ1+θ3)-l1*sin(θ1), -l3*sin(θ2+θ1+θ3), sin(θ1), l2*cos(θ2+θ1)+l3*cos(θ2+θ1+θ3)+l1*cos(θ1), l3*cos(θ2+θ1+θ3), 0, 1, 1])
print("Matrix A :")
pprint(A)
print(" ")
print(" Inverse Matrix - A1")
A1= A.inv()                  #inverse of Matrix A is determined
pprint(A1)                   # printing Matrix A1
print(" ")
print("The elements in the matrix A inverse",'\n')

for i in range(3):          #printing elements in the inverse matrix
    for j in range(3):
        print("A1 [",i,j,"]")
        print(A1[i,j])
