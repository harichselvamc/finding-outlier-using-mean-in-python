import pandas as pd
import numpy as np


x=pd.Series([2.1,2.2,4.5,2.7,2.3])


mean=np.mean(x)
print(mean)
std=np.std(x)
print(std)
outlier=[]
for items in x:
    if (items<mean-std)or (items> mean+std):
        outlier.append(items)
    
print(outlier)