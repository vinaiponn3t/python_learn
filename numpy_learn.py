#import numpy as np  
import matplotlib.pyplot as plt
from scipy import stats

# data = np.array([4,5,6,1,2,7,9,3,2,10,25,25,25,25])

# dt_mean = np.mean(data); print("Mean : ",round(dt_mean,2))

# dt_median = np.median(data); print("Median : ",dt_median )

# dt_mode = stats.mode(data); print ("Mode : ",dt_mode)

def demo():
    x=[170,165,180,155,163,160,175]
    y=[80,65,75,47,50,52,74]
    
    plt.scatter(x,y)
    plt.show()
    
if __name__ == '__main__':
    demo()