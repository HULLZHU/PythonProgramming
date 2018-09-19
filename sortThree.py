import random
import matplotlib.pyplot as plt


variable = [];
for i in range(10000):
    a = random.normalvariate(0,1)
    variable.append(a)

plt.title("Demo Normal Distribution")
plt.hist(variable,bins=100)
plt.show()



