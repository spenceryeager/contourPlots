import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
#UPDATED 07JUNE2021
#Used for Cary5000
# future directions:
# - expand "read_csv" to skip all header info, use header command in pandas

workingdir = '/run/user/1000/gvfs/sftp:host=file.engr.arizona.edu/Research/Ratcliff/Spencer/data/2021/06_Jun/09Jun2021_cary5000_transmission_curves_and_p3ht/p3ht_PF6/run2'
allfiles = os.listdir(workingdir)
filelist = []
for i in allfiles:
    if i.endswith(".csv"):
        filelist.append(i)
# print(filelist)

#this creates a list of potentials
potential_list = pd.read_csv(workingdir + '/' + 'potential_list.csv')
potential_array = potential_list.to_numpy()
# print(potential_array)

# #this creates a list of wavelengths that will be used.
datalist = pd.read_csv(workingdir + '/' + filelist[0], skiprows=1, skipfooter=28)
wavelength = datalist['Wavelength (nm)']
wavelength_array = wavelength.to_numpy()
# print(wavelength_array)

#
# #this creates a list of absorbance values at each potential
abs_total = []
for i in filelist:
    if i != 'potential_list.csv':
        working_data = pd.read_csv(workingdir + '/' + i, skiprows=1, skipfooter=28, usecols=['Abs'])
        data_array = working_data.to_numpy()
        abs_array = []
        for i in data_array:
            abs_array.append(i[0])
        abs_total.append(abs_array)
# print(abs_total)


# #This portion makes the graph
Y, X = np.meshgrid(wavelength_array, potential_list)

# levels are used to define the color bar axis.
levels = np.linspace(-0.2, 0.28, 10000)
plt.contourf(X, Y, abs_total, cmap='jet', levels = levels)
plt.xlabel("Potential (V)")
plt.ylabel("Wavelength (nm)")
plt.ylim(400,1500)
plt.colorbar(label="Absorbance (arb. units)")
plt.show()
