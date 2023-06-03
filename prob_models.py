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
weight = np.asarray(DF_H.weight)
height = np.asarray(DF_H.height)

Model_H.fit(weight.reshape(-1,1))
Model_H.fit(height.reshape(-1,1))

#Woman Model
weight = np.asarray(DF_M.weight)
height = np.asarray(DF_M.height)

Model_M.fit(weight.reshape(-1,1))
Model_M.fit(height.reshape(-1,1))


# weight_input = float(input("Enter your weight: "))
# weight_input = np.asarray(weight_input)

# gender = input("Inserte Genero: ")

# if gender == "H":
    
#     p = Model_H.predict_proba(weight.reshape(-1,1))
#     print(p)

# else:
    
#     p = Model_M.predict_proba(weight.reshape(-1,1))
#     print(p)

pickle.dump((Model_H, Model_M), open("TestFarma_Model_HW.p", "wb"))

print("Models saved successfully")
