import sys
import math

# the function to be integrated
def func(x):
    return 4.0 / (1 + x**2)

if __name__ == '__main__':

   if len(sys.argv) != 2:
     sys.exit('Define number of segments as argument.')	

   n = int(sys.argv[1])
   dx = float(1.0 / n)
   area = 0
   print(dx, n)
   # loop to calculate the area of each trapezoid and sum.
   for i in range(1, n+1):
       #the x locations of the left and right side of each trapezpoid
       x0 = (i-1)*dx
       x1 = i*dx

       #the area of each trapezoid
       ai = dx * (func(x0) + func(x1))/ 2.

       # cumulatively sum the areas
       area = area + ai

#print out the result.
   print("Area = ", area)
