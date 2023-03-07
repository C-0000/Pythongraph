import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np




x = np.linspace(1, 10, 100)
y = x**2
y2 = x+x
plt.plot(x, y, label='y = x^2', color='red', linewidth=2)
plt.plot(x, y2, label='y = x', marker='x')
plt.title('Gangmitglieder uber die jahre')
plt.grid(True)
plt.legend()
plt.show()