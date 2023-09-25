# ENPM662_HW1
Robot Modelling Kinematics

The path of front wheel of a bicycle in a 2 coordinate system is plotted
the 2D trajectory of point O on a simple bicycle,

initial pose (xi,yi,ϕi)

ω = rear wheel drive angular speed 
α = 0.5*sin(πt)     # Steering Angle
T = total time
The length of the bicycle D = 1.5
Diameter of wheel = o.5 meters
Assumptions made for this case :  These values can be changed as per requirements in the code

ω = 5 rad/sec 
T = 10 sec               
theta_1 = (0.5* pi)         # Initial theta 
x1 = 0                      # Initial X Coordinate
y1 = 0                      # Initial Y Coordinate
time_interval = 0.1         # Time Interval

For all the intervals, alpha values are computed. These alpha values with considered assumptions are considered for the loop.
The loop runs to determine x, y, theta at all instances, and x, y are plotted in the graph

The code outputs the path travelled in a XY-Plane

# ENPM662_HW1
the kinematics equations for a 3-DOF manipulator
sympy library is used to perfrom derivatives

Declaring :
l2, θ2, l3, t as constants 
θ1, l1, θ3 as functions wrt t

Considering Robot with 3 links connected by revolute and prismatic joints with the link lengths l1 (variable), l2, l3 and angles θ1, θ2 (fixed), θ3

The values for x, y, θ in terms of l1, l2, l3, θ1, θ2, θ3 is obtained in the documentation provided
This is given as input, and calculated x_dot, y_dot, θ_dot, differentiation wrt time t

The obtained values from this calculation is further written in matrix form and factorized to get the matrix equation in terms of l1_dot, θ1_dot, θ3_dot
This is named as matrix A
Inverse of A is calulated to get inverse kinematic equations in matrix form
