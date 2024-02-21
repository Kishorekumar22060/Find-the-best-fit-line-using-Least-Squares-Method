import numpy as np
import matplotlib.pyplot as plt
x =np.array(eval(input()))
y =np.array(eval(input()))

x_mean = np.mean(x)
y_mean = np.mean(y)
num,den=0,0

for i in range(len(x)):
  num +=(x[i]-x_mean)*(y[i]-y_mean)
  den += (x[i]-x_mean)**2
m=num/den
b=y_mean-m*x_mean
print(m,b)

y_predicted=m*x+b
print(y_predicted)

plt.scatter(x,y)
plt.plot(x,y_predicted,color='red')
plt.show()