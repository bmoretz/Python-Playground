#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 19:06:02 2018

@author: Jessica
"""

from __future__ import division, print_function

from sklearn.datasets import fetch_mldata

from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.metrics import f1_score

import matplotlib
import matplotlib.pyplot as plt

import csv
import time
import numpy as np
import pandas as pd

mnist = fetch_mldata('MNIST original', data_home='./')
mnist.data.shape
mnist

X, y = mnist['data'], mnist['target']
X.shape
y.shape

# Display 36,000th image
some_digit = X[36000]
some_digit_image = some_digit.reshape(28, 28)

plt.imshow(some_digit_image, cmap = matplotlib.cm.binary, 
           interpolation = 'nearest')

plt.axis('off')
plt.show()

# Split the data to 60,000 images as training data and 10,000 as test data
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]

# --- Random Forest Classifier ---
rfClf = RandomForestClassifier(n_estimators=100, max_leaf_nodes=10, n_jobs=-1)    

# Record the time it takes to fit the model
# set random number seed 
np.random.seed(seed = 9999)

replications = 10  # repeat the trial ten times
x_time = [] # empty list for storing test results
n = 0  # initialize count
print('--- Time to Fit Random Forest Classifier ---')
while (n < replications): 
    start_time = time.clock()
    # generate 1 million random negative binomials and store in a vector
    rfClf.fit(X_train, y_train)
    end_time = time.clock()
    runtime = end_time - start_time  # seconds of wall-clock time
    x_time.append(runtime * 1000)  # report in milliseconds 
    print("replication", n + 1, ":", x_time[n], "milliseconds\n") 
    n = n + 1

# write results to external file 
with open('rf_fit.csv', 'wt') as f:
    writer = csv.writer(f, quoting = csv.QUOTE_NONNUMERIC, dialect = 'excel')
    writer.writerow('x_time')    
    for i in range(replications):
        writer.writerow(([x_time[i],]))

# preliminary analysis for this cell of the design
print(pd.DataFrame(x_time).describe())

y_predict = rfClf.predict(X_test)

# Performance measurement using F1-score
f1Score = f1_score(y_test, y_predict, average='weighted')
print('\nF1 Score: ', f1Score)

# --- PCA ---

# Generate principal components that represent 95 percent of the variability
# in the explanatory variables
pca = PCA(n_components=0.95)

# Runtime to identify the principal components
pca_time = [] # empty list for storing test results
n = 0  # initialize count
print('--- Time to Identify Pricipal Components ---')
while (n < replications): 
    start_time = time.clock()
    # generate 1 million random negative binomials and store in a vector
    X_pca = pca.fit_transform(X) # run on all 70,000 observations
    end_time = time.clock()
    runtime = end_time - start_time  # seconds of wall-clock time
    pca_time.append(runtime * 1000)  # report in milliseconds 
    print("replication", n + 1, ":", pca_time[n], "milliseconds\n") 
    n = n + 1

# write results to external file 
with open('pca_fit.csv', 'wt') as f:
    writer = csv.writer(f, quoting = csv.QUOTE_NONNUMERIC, dialect = 'excel')
    writer.writerow('pca_time')    
    for i in range(replications):
        writer.writerow(([pca_time[i],]))
# -- Results: Dimension is reduced to 154 variables from 784 variables
print(pd.DataFrame(pca_time).describe())

# show summary of pca solution
pca_explained_variance = pca.explained_variance_ratio_
print('Proportion of variance explained:', pca_explained_variance)

# Split the reduced data to 60,000 images as training data and 10,000 as test data
X_pca_train, X_pca_test = X_pca[:60000], X_pca[60000:]

# Random Forest Classifier using the principal components
rfClf_pca = RandomForestClassifier(n_estimators=100, max_leaf_nodes=10, n_jobs=-1)

# Runtime to identify the principal components
x_pca_time = [] # empty list for storing test results
n = 0  # initialize count
print('--- Time to Fit Random Forest Classifier using Principal Components ---')
while (n < replications): 
    start_time = time.clock()
    # generate 1 million random negative binomials and store in a vector
    rfClf_pca.fit(X_pca_train, y_train)
    end_time = time.clock()
    runtime = end_time - start_time  # seconds of wall-clock time
    x_pca_time.append(runtime * 1000)  # report in milliseconds 
    print("replication", n + 1, ":", x_pca_time[n], "milliseconds\n") 
    n = n + 1

# write results to external file 
with open('rf_pca_fit.csv', 'wt') as f:
    writer = csv.writer(f, quoting = csv.QUOTE_NONNUMERIC, dialect = 'excel')
    writer.writerow('x_pca_time')    
    for i in range(replications):
        writer.writerow(([x_pca_time[i],]))

print(pd.DataFrame(x_pca_time).describe())

y_predict_pca = rfClf_pca.predict(X_pca_test)

# Performance measurement using F1-score
f1Score_pca = f1_score(y_test, y_predict_pca, average='weighted')
print('\nF1 Score: ', f1Score_pca)

