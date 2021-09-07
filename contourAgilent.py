import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter.filedialog as fd
from tkinter import *
import os

#UPDATED 27JULY2021
#Used for Agilent spectrometer in ECE
# future directions:
# - expand "read_csv" to skip all header info, use header command in pandas

root = Tk()
root.withdraw()

# workingdir = '/run/user/1000/gvfs/sftp:host=file.engr.arizona.edu/Research/Ratcliff/Spencer/data/2021/06_Jun/02Jun2021_spectroelectrochemistry_P3HT_pf6/potential_abs_studies'
workingdir = fd.askdirectory(initialdir="/home/spenceryeager/Documents/python_bits/contour_plot/agilent")
filelist = os.listdir(workingdir)
filelist.sort()
for i in filelist:
    print(i)

# this creates a list of potentials
potential_list = pd.read_csv(workingdir + '/' + 'potential_list.csv', header=None)
potential_array = potential_list.to_numpy()
print('potential list total')
print(len(potential_array))

for i in potential_array:
    print(i)
# this creates a list of wavelengths that will be used.
datalist = pd.read_csv(workingdir + '/' + '000V.CSV')
wavelength = datalist['Wavelength (nm)']
wavelength_array = wavelength.to_numpy()

print("weavelength length")
print(len(wavelength_array))


#this creates a list of absorbance values at each potential
abs_total = []
for i in filelist:
    if i != 'potential_list.csv':
        working_data = pd.read_csv(workingdir + '/' + i, usecols=['Absorbance (AU)'])
        data_array = working_data.to_numpy()
        abs_array = []
        for i in data_array:
            abs_array.append(i[0])
        abs_total.append(abs_array)

print("absorbance length total")
print(len(abs_total))

#This portion makes the graph
Y, X = np.meshgrid(wavelength_array, potential_list)

# levels are used to define the color bar axis.
levels = np.linspace(0.0, 0.29, 500)
plt.contourf(X, Y, abs_total, cmap='jet', levels=levels, extend='min')
plt.xlabel("Potential (V)")
plt.ylabel("Wavelength (nm)")
plt.ylim(400,1000)
plt.colorbar(label="Absorbance (arb. units)")
plt.show()
