
# import the packages needed for this code
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

# define path
path = r"E:\Universite\Matrise\Article - Comparison\AnsysWorking\Stiffness"
os.chdir( path )

# load the data from the csv file as a data fram in pandas
df_CoordinateData = pd.read_csv('Data1.csv',  header=None)
df_CoordinateData.columns = ['CoordinateNum','Orientation']

df_ElmData = pd.read_csv('DataElm1.csv',  header=None)
df_ElmData.columns = ['ElementNum','CoordinateNum']

# assigne orientation to element number
df = df_ElmData.merge(df_CoordinateData, on='CoordinateNum')
df.sort_values(by=['ElementNum'], inplace=True, ascending=True)
data = df[df['Orientation'] <= 90]
Theta = data['Orientation'].to_numpy()

theta = np.sqrt(Theta**2)
x = np.cos(np.deg2rad(theta))
y = np.sin(np.deg2rad(theta))
AbsU = np.sqrt((x**2) + (y**2))

a11 = x/AbsU
a22 = y/AbsU



# plot histograme
fig, axs = plt.subplots()
axs.hist(Theta, 25, density=True, facecolor='k', alpha=0.75)
plt.xlabel('Fibre orientation (°)')
plt.ylabel('Probability')
plt.show()
