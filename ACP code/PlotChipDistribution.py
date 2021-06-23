# This codes regerates a heat plot of the chip distribution for each ply of the composite

# import the packages needed for this code
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load the data from the csv file as a data fram in pandas
df = pd.read_csv(r'E:\Universite\Matrise\Article - Comparison\WorkbenchWorking\ACP code\LookUpData.csv',  header=None)

df.columns = ["Location.x", "Location.y", "Location.z", "Ply0", "Ply1", "Ply2", "Ply3", "Ply4", "Ply5", "Ply6", "Ply7", "Ply8", "Ply9", "Ply10", "Ply11","Ply12", "Ply13", "Ply14", "Ply15", "Ply16", "Ply17"]

# What ply to show orientation
n = 18
Orientation = df['Ply'+str(n-1)]
Xposition = df['Location.x']
Yposition = df['Location.y']

# Reshape the data
X = len(np.unique(Xposition))
Y = len(np.unique(Yposition))
Orientation = Orientation.to_numpy().reshape((Y, X))
Orientation = np.flip(Orientation,1)
#Orientation = Orientation.T

# get the orientation of all the element
AllOrientation = df.to_numpy()
AllOrientation = AllOrientation[:,3:21]
AllAngles = np.reshape(AllOrientation, X*Y*18)

# plot the data
fig, ax = plt.subplots()
c = plt.imshow(Orientation, cmap='Greys', interpolation='nearest')
fig.colorbar(c, ax=ax)
plt.title('Ply number = '+str(n))

# plot histograme
fig, axs = plt.subplots()
axs.hist(AllAngles, 25, density=True, facecolor='k', alpha=0.75)

# show all graphs
plt.show()