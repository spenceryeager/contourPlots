import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
#UPDATED 07JUNE2021
#Used for Ocean Optics
# future directions:
# - expand "read_csv" to skip all header info, use header command in pandas

workingdir = '/run/user/1000/gvfs/sftp:host=file.engr.arizona.edu/Research/Ratcliff/Spencer/data/2021/06_Jun/02Jun2021_spectroelectrochemistry_P3HT_pf6/potential_abs_studies'
filelist = os.listdir(workingdir)

#this creates a list of potentials
potential_list = pd.read_csv(workingdir + '/' + 'potential_list.csv')
potential_array = potential_list.to_numpy()

#this creates a list of wavelengths that will be used.
datalist = pd.read_csv(workingdir + '/' + '000V.txt', sep='\t')
wavelength = datalist['Absorbance:209']
wavelength_array = wavelength.to_numpy()


#this creates a list of absorbance values at each potential
abs_total = []
for i in filelist:
    if i != 'potential_list.csv':
        working_data = pd.read_csv(workingdir + '/' + i, sep='\t', usecols=['Unnamed: 1'])
        data_array = working_data.to_numpy()
        abs_array = []
        for i in data_array:
            abs_array.append(i[0])
        abs_total.append(abs_array)



#This portion makes the graph
Y, X = np.meshgrid(wavelength_array, potential_list)

# levels are used to define the color bar axis.
levels = np.linspace(0.0, 0.31, 300)
plt.contourf(X, Y, abs_total, cmap='jet', levels=levels)
plt.xlabel("Potential (V)")
plt.ylabel("Wavelength (nm)")
plt.ylim(400,1000)
plt.colorbar(label="Absorbance (arb. units)")
plt.show()
