from matplotlib import pyplot as plt
import pandas as pd                                               
corona=pd.read_csv("full_data.csv")
corona=pd.DataFrame(corona)
x=corona["total_cases"]
y=corona["weekly_cases"]
plt.plot(corona["total_cases"], corona["weekly_cases"])

plt.scatter(x,y)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
corona=pd.read_csv("full_data.csv")
corona.plot.scatter(x="total_cases", y="weekly_cases")
plt.show()



