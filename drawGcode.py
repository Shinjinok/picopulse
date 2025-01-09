from matplotlib import pyplot as plt
import numpy as np

x0=  50
y0 = 50
z0 = 10
width = 50
height = 100
lines = 10
direction = "holizental"
x= []
y=[]

for i in range(lines):
    x.append(width/lines*i + x0)
    x.append(width/lines*i + x0)
for i in range(lines):
    d= i%2
    if d == 0:
        y.append(y0)
        y.append(height+y0)    
    else :
        y.append(height+y0)
        y.append(y0)    


plt.plot(x,y)
plt.show()

f = open("strainGcode.gcode", 'w')
data =  "G90\nM3 S0\nG21\nM3 S0\nG1 F3000 X"+str(x0)+ " Y"+str(y0)+" Z"+str(z0)+"\nM3 S255\nG1 F1500\n"
f.write(data)
for i in range(len(x)-1):
    data = "G1 X"+str(x[i+1])+ " Y"+str(y[i+1])+"\n"
    f.write(data)
f.close()

