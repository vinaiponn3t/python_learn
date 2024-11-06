import numpy as np
from statistics import variance,stdev
print(stdev)
point = [35,56,43,59,63,79,35,41,64,43,93,60,77,24,82,55,78,96]
game_points = np.array(point)

#calculate variance
dt_var = variance(game_points);  
print("Sample variance :",round(dt_var,4))
#calculate standard deviation
dt_std = stdev(point);  
print("Sample std.dev:",round(dt_std,2))

#calculate range
dt_range = np.max(game_points,axis=0)-np.min(game_points,axis=0)
print ("range : ",dt_range)

#calculate percentiles
print("Quantiles")
for val in [20,25,75,80,100]:
    dt_qntls = np.percentile(game_points,val)
    print (str(val)+"% : ",dt_qntls)
    
#calculate IQR
q75,q25 = np.percentile(game_points, [75,25]); print("Interquartile range : ",q75-q25)