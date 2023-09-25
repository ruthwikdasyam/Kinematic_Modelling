import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, pi 

#----------------defining variables

Diameter_wheel = 0.5
ω = 5
v = ω*(Diameter_wheel)  # Velocity = Omega * Radius 
D = 1.5                     # Length of Cycle in meters

θ1 = round((0.5* pi),3)              # Initial θ 
x1 = 0                      # Initial X Coordinate
y1 = 0                      # Initial Y Coordinate
T = 12                   # total duration
time_interval = 0.1       # Time Interval

#--------------- Finding alpha at all instances in time T

alpha=[]
t=np.arange(0,T,time_interval)
for i in t:
    alpha.append(0.5*sin(pi*i))     # alpha = 0.5 sin(pi*t)

#--------------- Finding x, y, θ positions at all instances

θ=[]                        #creating an array to store θ values at all instances
x=[]                        #creating an array to store x values at all instances
y=[]                        #creating an array to store y values at all instances

for i in range(len(t)):
    θ.append(θ1)
    θ2=θ1+ round(time_interval*(v/cos(alpha[i])*sin(alpha[i])/D), 3)         # Formula to obtain θ2 from θ1, as given in documentation
    x.append(x1)
    x2 = x1 + time_interval*(v/cos(alpha[i])*cos(θ2 - alpha[i]))             # Formula to obtain x_2 from x_1, as given in documentation
    y.append(y1)
    y2 = y1 + time_interval*(v/cos(alpha[i])*sin(θ2 - alpha[i]))             # Formula to obtain y_2 from y_1, as given in documentation
    θ1 = θ2                                                                  # here θ2 is the θ obtained at time t+ dt
    x1 = x2                                                                  # x2 is value of X at time t + dt
    y1 = y2

#------------- Plotting values of X and Y on the 2D graph
plt.plot(x,y) 
plt.title("2D trajectory of point O")
plt.xlabel("Distance in X")
plt.ylabel("Distance in Y")
plt.show()                    #Displaying the graph as output