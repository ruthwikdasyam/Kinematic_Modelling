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
