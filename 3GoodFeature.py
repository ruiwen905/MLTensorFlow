import numpy as np
import matplotlib.pyplot as plt

#create 1000 dogs
greyhounds = 500
labs = 500

#set height random 28/24 +- 4 inches
grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 24 + 4 * np.random.randn(labs)

#plot histogram, greyhounds in red, labradors in blue
plt.hist([grey_height, lab_height] , stacked=True, color=['r','b'])
plt.show()