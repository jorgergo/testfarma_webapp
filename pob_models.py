import pandas as pd
from sklearn.mixture import GaussianMixture
import numpy as np
import pickle

DF = pd.read_csv('cardio_train.csv', sep=';')

DF_H = DF[DF.gender == 1];
DF_M = DF[DF.gender == 2];

Model_H = GaussianMixture(n_components = 3)
Model_M = GaussianMixture(n_components = 3)

X = np.asarray(DF_H.weight)

Model_H.fit(X.reshape(-1,1))

X = np.asarray(DF_M.weight)

Model_M.fit(X.reshape(-1,1))

weight = float(input("Enter your weight: "))
weight = np.asarray(weight)

gender = input("Inserte Genero: ")

if gender == "H":
    
    p = Model_H.predict_proba(weight.reshape(-1,1))
    print(p)

else:
    
    p = Model_M.predict_proba(weight.reshape(-1,1))
    print(p)

pickle.dump((Model_H, Model_M), open("TestFarma.p", "wb"))

