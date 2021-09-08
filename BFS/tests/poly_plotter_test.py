import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,12,100)

fx = []
for i in range(len(x)):
    fx.append(-3.554318e+02+9.461590e+02*x[i]-8.375958e+02*x[i]**2+3.640662e+02*x[i]**3-8.735626e+01*x[i]**4+1.214157e+01*x[i]**5-9.741451e-01*x[i]**6+4.191430e-02*x[i]**7-7.495953e-04*x[i]**8)

plt.plot(x,fx)
plt.show()
