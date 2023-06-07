import pandas as pd
from sklearn.mixture import GaussianMixture
import numpy as np
import pickle

#Read CSV
DF = pd.read_csv('cardio_train.csv', sep=';')

#Retrieve data from CSV
DF_H = DF[DF.gender == 1];
DF_M = DF[DF.gender == 2];

print(DF_H)
print(DF_M)

#Initialize Models
Model_H = GaussianMixture(n_components = 3)
Model_M = GaussianMixture(n_components = 3)


#Man Model
vars_h = np.asarray(DF_H[["weight", "height"]])

print(vars_h)

Model_H.fit(vars_h)

#Woman Model
vars_m = np.asarray(DF_M[["weight", "height"]])

Model_M.fit(vars_m)

pickle.dump((Model_H, Model_M), open("TestFarma_Model_HW.p", "wb"))

print("Models saved successfully")
