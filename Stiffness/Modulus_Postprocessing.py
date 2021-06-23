import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------ load the data ----------------------------------------
# Baseline UD
dataUni = pd.read_csv(r'E:\Universite\Matrise\Article - Comparison\AnsysWorking\Stiffness\UD_BaseLine\ModulusResults.csv')
ModuleUni = dataUni[' Module(GPA)']

# Longitudinal UD
dataFav = pd.read_csv(r'E:\Universite\Matrise\Article - Comparison\AnsysWorking\Stiffness\UD_Longitudinal\ModulusResults.csv')
ModuleFav = dataFav[' Module(GPA)']

# transverse UD
dataUnFav = pd.read_csv(r'E:\Universite\Matrise\Article - Comparison\AnsysWorking\Stiffness\UD_Transverse\ModulusResults.csv')
ModuleUnfav = dataUnFav[' Module(GPA)']

# Baseline Woven
dataUni_W = pd.read_csv(r'E:\Universite\Matrise\Article - Comparison\AnsysWorking\Stiffness\W_BaseLine\ModulusResults.csv')
ModuleUni_W = dataUni_W[' Module(GPA)']

# Longitudinal Woven
dataFav_W = pd.read_csv(r'E:\Universite\Matrise\Article - Comparison\AnsysWorking\Stiffness\W_Longitudinal\ModulusResults.csv')
ModuleFav_W = dataFav_W[' Module(GPA)']

# Transverse Woven
dataUnFav_W = pd.read_csv(r'E:\Universite\Matrise\Article - Comparison\AnsysWorking\Stiffness\W_Transverse\ModulusResults.csv')
ModuleUnfav_W = dataUnFav_W[' Module(GPA)']

# -------------------------------------- Create a dataframe with all the data ---------------------------------------------------
# arrange the data in a dataframe with pands
df = pd.concat([ModuleUni, ModuleFav, ModuleUnfav, ModuleUni_W, ModuleFav_W, ModuleUnfav_W], axis=1, join="inner")
df.columns = ["Baseline UD", "Longitudinal UD", "Transverse UD", "Baseline Woven", "Longitudinal Woven", "Transverse Woven"]

# -------------------------------------- Statistical analysis on the df ---------------------------------------------------------
M = df.mean()
S = df.std()
CoV = (S/M) * 100
print(df)

# -------------------------------------- Plot the results ------------------------------------------------------------------------
sns.boxplot(x="variable", y="value", data=pd.melt(df))
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70])
plt.ylabel('Stiffness (GPa)')
plt.xlabel('Specimen type')
plt.show()

