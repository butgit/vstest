from math import radians
import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt
import sys
my_var = 'CODE Magazine' # we want to test this
def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()
if __name__ == '__main__':
    main()
