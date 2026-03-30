import random
import math
n= int(input("Enter number of itterations: "))
step = int(input("Enter number of steps: "))
count_points=0
for i in range(1,n+1):
     x= random.random()
     y= random.random()

     if x**2 + y**2 <=1:
        count_points +=1


     if i % step ==0:
        pi_estimate =  4 * count_points/i
        print(f"Iteration {i} the value of Pi ≈ {pi_estimate}")
print(f"Final approximation: {4*count_points/n}")
print(f"Math.Pi: {math.pi}")